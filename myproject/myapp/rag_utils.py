from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain_community.vectorstores.utils import filter_complex_metadata
import os
load_dotenv()

# Chroma veritabanı dizini
persist_directory = "db"

def veritabanıVarMı():
    # Eğer veritabanı zaten varsa, onu yükle
    if os.path.exists(persist_directory):
        print("Mevcut veritabanı yükleniyor...")
        chroma = Chroma(
            persist_directory=persist_directory,
            embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        )
    else:
        print("Yeni veritabanı oluşturuluyor...")
        # Excel dosyasını yükle
        loader = UnstructuredExcelLoader(file_path="myproject/soru_cevaplar.xlsx", mode="elements")
        documents = loader.load()

        # Karmaşık metadata'ları filtrele
        documents = filter_complex_metadata(documents)

        # Google Generative AI Embedding modelini kullanarak embedding'ler oluşturuluyor.
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

        # Belgeler üzerinde embedding'leri kullanarak Chroma ile vektör arama yapmak için bir yapı oluşturulur
        chroma = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            persist_directory=persist_directory
        )
        chroma.persist()  # Veritabanını kaydet

    # RAG zincirini oluştur
    retriever = RunnableLambda(chroma.similarity_search).bind(k=2)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

    message = """
    lütfen sadece sana verilen belgeden cevaplar oluştur bunun dışında bir soru soruluyorsa bilmiyorum falan de yapabileceğin şeyler hakkında 2 satır bir bilgi ver uzun uzun her şeyi getirme
    Cevabı türkçe ve olabildiğince kısa ver.  
    İnsanlara yardımcı olmak için oluşturuldun buna göre cevaplar ver.
    Görsellik kat biraz ve daha samimi ol.

    {question}

    Context:
    {context}
    """

    prompt = ChatPromptTemplate.from_messages([("human", message)])
    rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm
    
    return rag_chain

# RAG zincirini global olarak tut
rag_chain = veritabanıVarMı()

def get_rag_response(question):
    try:
        response = rag_chain.invoke(question)
        return str(response.content)
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}" 