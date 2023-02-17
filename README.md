# Backend

### Pasos:
1. Tener Python instalado y la BD SQLite (https://sqlitebrowser.org/dl/)
2. Opcional crear un virtualenv a la altura de la carpeta raiz del repo y activarlo
3. Moverse a la carpeta backend_challenge
4. Instalar Django `pip install Django==4.1.7`
5. Instalar Rest Framework `pip install djangorestframework`
6. Abrir SQLite --> open database --> seleccionar db.sqlite3 (está en el repo).
Esto debería hacer que al abrir la BD ya se tengan casos de ejemplo, de ser así, saltar al paso 9, sino seguir por el paso 7.
7. Abrir shell `python manage.py shell`
8. Poner en la shell todas las líneas del archivo 'data.txt' para tener elementos de ejemplo en la BD
9. Levantar servidor `python manage.py runserver`
10. Probar endpoints:
    - http://localhost:8000/api/users
    - http://localhost:8000/api/friendships

### Cosas para mejorar:
1. La forma en la que hice el endpoint del punto 'List all friendships registered in the system', seguro hay una consulta más facil que lo resuelve sin hacer tantos for.
2. Que en el endpoint http://localhost:8000/api/friendships si se muestra que paula es amiga de tomas, no se muestre la viceversa.



