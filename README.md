## Installation

- Allez dans le dossier `backend/`.
- Créez un environnement virtuel avec `python3 -m virtualenv env` ou `python -m virtualenv env` ou encore `py -m virtualenv env`.
- Activez votre environnement avec `source env/bin/activate` ou `env\Scripts\activate.bat`.
- Installez les modules `pip install -r requirements.txt`.
- Faites vos migrations avec `python manage.py migrate` ou `py manage.py migrate`.

#### N.B
- Pendant l'installation, il risque d'y avoir une erreur lors de la création de la BDD. Pour la résoudre, il faut commenter la classe `StandardResultsSetPagination` de `backend/servers/views.py` et commenter la ligne `pagination_class` du même fichier, le temps de faire les migrations.
- Il faut également créer un fichier `backend/tensor_site/auth_tokens.py` en suivant le modèle de `backend/Tensor/auth_tokens_sample.txt`.