Some info abot steps

1. Install python, vscode, create virtual env

python3.12 -m venv venv_blog
source venv/bin/activate
pip3.12 freeze # shows installed packages

2. Install FastAPI

pip3.12 install "fastapi[all]"

3. Path operation, znana również jako route operation lub endpoint, to jedna z podstawowych koncepcji w FastAPI. Jest to określony punkt końcowy w Twojej aplikacji, który jest dostępny przez HTTP. Każda operacja ścieżki jest powiązana z konkretnym adresem URL, metodą HTTP (np. GET, POST, PUT, DELETE) i funkcją, która ma zostać wykonana, gdy operacja ścieżki jest wywoływana.

W Twoim fragmencie kodu, @app.get("/") definiuje operację ścieżki. Oznacza to, że gdy użytkownik odwiedzi adres URL Twojej aplikacji z dodatkowym "/", i wyśle żądanie GET, funkcja root() zostanie wywołana.

```
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