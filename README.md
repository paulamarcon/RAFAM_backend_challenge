# Backend

### Pasos:
1. Tener Python instalado
2. Opcional crear un virtualenv
3. Instalar Django `pip install Django==4.1.7`
4. Instalar Rest Framework `pip install djangorestframework`
5. Ejecutar `python manage.py migrate`
6. Abrir shell `python manage.py shell`
7. Poner en la shell todas las líneas del archivo 'data.txt' para tener elementos de ejemplo en la BD
8. Levantar servidor `python manage.py runserver`
9. Probar endpoints:
    - http://localhost:8000/api/users
    - http://localhost:8000/api/friendships

### Cosas para mejorar:
1. La forma en la que hice el endpoint del punto 'List all friendships registered in the system', seguro hay una consulta más facil que lo resuelve sin hacer tantos for


