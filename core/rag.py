from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document


def criar_documentos(transacoes=None, historico=None, produtos=None, perfil=None):
    docs = []

    if transacoes is not None and not transacoes.empty:
        for row in transacoes.to_dict(orient="records"):
            docs.append(Document(
                page_content=f"{row.get('categoria')} {row.get('valor')} {row.get('tipo')}",
                metadata={"source": "transacoes"}
            ))

    if historico is not None and not historico.empty:
        for row in historico.to_dict(orient="records"):
            docs.append(Document(
                page_content=f"{row.get('tema')} {row.get('resumo')}",
                metadata={"source": "historico"}
            ))

    return docs


def criar_vector_db(docs):
    if not docs:
        return None

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return FAISS.from_documents(docs, embeddings)


def buscar_contexto(query, vector_db, k=4):
    if vector_db is None:
        return ""

    try:
        resultados = vector_db.similarity_search(query, k=k)
        return "\n".join([r.page_content for r in resultados])
    except:
        return ""