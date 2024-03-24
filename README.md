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
10. CRUD - CREATE, READ, UPDATE, DELETE, 
    put i patch różnią sie tym ze w put musimy podac wszystkie pola które chcemy zmienić a w patch tylko te co chemy zmienić

11. We can keep our posts in array, (will change it later)

    ```python
    my_posts = [{"title": "Post 1", "content": "This is the content of post 1", "published": True, "rating": 5},
            {"title": "Post 2", "content": "This is the content of post 2", "published": False, "rating": 4},
            {"title": "Post 3", "content": "This is the content of post 3", "published": True, "rating": 3}]
    ```
12. Creating one post

    get_post, która przyjmuje jeden argument id o typie int i to waliduje, jak damy jakiegos stringa to fastAPI zwróci nam błąd z informacja zamiast internal error server

    ```python
    @app.get("/posts/{id}")
    def get_post(id: int):
        post = find_post(int(id))
        return {"post_detail": post}
    ```
13. Status code

    we can set status code using exception, we have to `import from fastapi, responses, status, HTTPException` additionally, in code we have to raise exception,  

    ```python
    @app.get("/posts/{id}")
    def get_post(id: int, response: responses.Response):
        post = find_post(int(id))
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
        return {"post_detail": post}

14. Update post

    - Deklaruje funkcję update_post z parametrami id (typu int), post (typu Post) i response (typu responses.Response).
    - Wywołuje funkcję find_index_post(id) w celu znalezienia indeksu posta o podanym identyfikatorze.
    - Jeśli indeks jest równy None, czyli post nie został znaleziony, podnosi wyjątek HTTPException z kodem statusu 404 i komunikatem "Post not found".
    - Tworzy słownik post_dict na podstawie modelu post i przypisuje mu identyfikator id.
    - Aktualizuje post o podanym indeksie w liście my_posts za pomocą słownika post_dict.
    - Zwraca odpowiedź JSON zawierającą wiadomość "message" i zaktualizowany post.
  
    Warto zauważyć, że ten kod korzysta z wcześniej zdefiniowanych klas i funkcji, takich jak Post

    ```python
    @app.put("/posts/{id}")
    def update_post(id: int, post: Post, response: responses.Response):
        index = find_index_post(id)
        if index == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
        post_dict = post.model_dump()
        post_dict["id"] = id
        my_posts[index] = post_dict
        return{"message": post_dict}
    ```
15. Install postgress on local machine and play with it (Create DB, create tables, add/remove items etc)

    Some Queryies I playes with
    ```sql
    select id AS products_id from products;
    select id AS products_id, price from products WHERE price >= 50;
    select * from products WHERE inventory != 0 AND price > 20;
    select * from products WHERE id IN (1,2,3);
    SELECT * FROM products WHERE name LIKE 'tv%';
    SELECT * FROM products WHERE name LIKE '%e';
    SELECT * FROM products WHERE name NOT LIKE '%e%';
    select id AS products_id from products ORDER BY price DESC;
    SELECT * from products ORDER BY id LIMIT 5 OFFSET 2;
    INSERT INTO products (name, price, inventory) VALUES ('something', 4, 100) returning *;
    DELETE FROM products WHERE id = 9 returning *;
    UPDATE products SET name = 'Laptop', price = 555 WHERE id = 2;
    UPDATE products SET is_sale = true WHERE id > 2 returning *;
    ```
16. Connect fastapi to postgress using psycopg2

    we can use this doc as a reference how to do it https://www.psycopg.org/docs/usage.html
    Poniższy kod:
    Ten kod łączy się z lokalną bazą danych PostgreSQL o nazwie "fastapi" przy użyciu użytkownika "postgres" i hasła "postgres". Tworzy również kursor z fabryką kursorów RealDictCursor, który zwraca wyniki zapytań jako słowniki. Jeśli połączenie jest udane, wyświetla komunikat "Connected to the database!!!". W przypadku wystąpienia błędu podczas połączenia, wyświetla komunikat "Error while connecting to PostgreSQL" wraz z informacją o błędzie.

    ```python
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="postgres",
            cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Connected to the database!!!")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    ```
17. ORM - zamiast pisania SQL zapytan można uzyć jezyka python
    I will ise Sqlalchemy - one of most populatr python ORM

    SQL Alchemy jaki stworzyc tabele, polaczenie do bazy z fastapi
    1. Stworzenie pliku database.py z informacjami o bazie
    2.  stworzenie pliku models.py gdzie jest informacja o tabelach
    3.  połączenie do bazy w samym pliku main.py (import modułów, zdefiniowanie funkcji get_db która obsóługuje połaczenie)
    4.  Refaktoryzacja kodu

    ```python
    # to tworzy tabele w bazie danych
    models.Base.metadata.create_all(bind=engine)

    # dzieki temu mozemy robic query na bazie
    @app.get("/sqlalchemy")
    def test_posts(db: Session = Depends(get_db)):
    return {"message": "Hello SQLAlchemy"} 
    ```

Link references:
- [HTTP requests methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [psycopg2](https://pypi.org/project/psycopg2/)

Tools:
- Postman
- Pydantic
- psycopg2 - connection between postgress and fastapi
- sqlalchemy - python ORM
- alembic - not used in this project, for migration in databases

Definitions:
- CRUD
- Pydantic
- ORM - Object Reliational Mapper - sits between database and us 
- DBMS - sits between app and database
