Some info abot steps

1. Install python, vscode, create virtual env

python3.12 -m venv venv_blog
source venv/bin/activate
pip3.12 freeze # shows installed packages

2. Install FastAPI

pip3.12 install "fastapi[all]"

3. Path operation, znana również jako route operation lub endpoint, to jedna z podstawowych koncepcji w FastAPI. Jest to określony punkt końcowy w Twojej aplikacji, który jest dostępny przez HTTP. Każda operacja ścieżki jest powiązana z konkretnym adresem URL, metodą HTTP (np. GET, POST, PUT, DELETE) i funkcją, która ma zostać wykonana, gdy operacja ścieżki jest wywoływana.

W Twoim fragmencie kodu, @app.get("/") definiuje operację ścieżki. Oznacza to, że gdy użytkownik odwiedzi adres URL Twojej aplikacji z dodatkowym "/", i wyśle żądanie GET, funkcja root() zostanie wywołana.

```python
@app.get("/")  # Definicja operacji ścieżki
async def root():  # Funkcja do wywołania, gdy operacja ścieżki jest wywoływana
    return {"message": "Hello World"}  # Zwraca słownik, który FastAPI automatycznie przekształca na JSON
```

4. Dekorator to funkcja wyższego rzędu, która przyjmuje inną funkcję jako argument i zwraca jeszcze inną funkcję, dodając do niej dodatkową funkcjonalność. W Pythonie, dekoratory są zazwyczaj używane do modyfikowania zachowania funkcji lub klasy.

W podanym przez Ciebie fragmencie kodu, `@app.get("/")` jest dekoratorem. Dekorator ten jest dostarczany przez FastAPI i mówi aplikacji, że funkcja `root()` powinna być wywoływana, gdy użytkownik odwiedzi ścieżkę "/" (stronę główną) i wykonuje żądanie GET. FastAPI automatycznie przekształca zwracany słownik na format JSON.

Oto jak to działa:

```python
@app.get("/")  # Dekorator
async def root():  # Funkcja, która jest dekorowana
    return {"message": "Hello World"}  # Zwraca słownik, który FastAPI automatycznie przekształca na JSON
```

Dekoratory są potężnym narzędziem w Pythonie, które pozwala na modyfikowanie i rozszerzanie zachowania funkcji i klas w łatwy i czytelny sposób.


5. Install Postman to test paths
6. read about HTTP requests methods

7. Extract data provided in body in postman
 Body(...) extracts all fields from body -> convert to python dict and store in variable
the we can terutn values from dict    

```python
@app.post("/create_posts")
def create_posts(payload: dict = Body(...)):
    return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}
```

9. Pydantic - data validation library for Python.

we need to first import pydantic
below code created model fol model and validate it
I also used method to convert pydantic to dict in print function
```python
# this validates if the user provides the correct data type
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.post("/createposts")
def create_posts(post: Post):
    print(post) # this will print the pydantic model
    print(post.dict()) # this will conver pydantic model to dictionary
    return {"data": post}
```


Link referances
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods # HTTP requests methods
- https://docs.pydantic.dev/latest/



Tools 
- Postman
- pydantic