## Project Documentation

## Project Documentation

1. Install python, vscode, create virtual env

    ```bash
    python3.12 -m venv venv_blog
    source venv/bin/activate
    pip3.12 freeze # shows installed packages
    ```

2. Install FastAPI

    ```bash
    pip3.12 install "fastapi[all]"
    ```

3. Path operation, znana również jako route operation lub endpoint, to jedna z podstawowych koncepcji w FastAPI. Jest to określony punkt końcowy w Twojej aplikacji, który jest dostępny przez HTTP. Każda operacja ścieżki jest powiązana z konkretnym adresem URL, metodą HTTP (np. GET, POST, PUT, DELETE) i funkcją, która ma zostać wykonana, gdy operacja ścieżki jest wywoływana.

    W Twoim fragmencie kodu, `@app.get("/")` definiuje operację ścieżki. Oznacza to, że gdy użytkownik odwiedzi adres URL Twojej aplikacji z dodatkowym "/", i wyśle żądanie GET, funkcja `root()` zostanie wywołana.

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
    `Body(...)` extracts all fields from body -> convert to python dict and store in variable
    then we can return values from the dict.

    ```python
    @app.post("/create_posts")
    def create_posts(payload: dict = Body(...)):
        return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}
    ```

9. Pydantic - data validation library for Python.

    First, we need to import pydantic. The code below creates a model for validation and uses a method to convert pydantic to a dict in the print function.

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
        print(post.dict()) # this will convert pydantic model to dictionary
        return {"data": post}
    ```
10. CRUD - CREATE, READ, UPDATE, DELETE


Link references:
- [HTTP requests methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)

Tools:
- Postman
- Pydantic

