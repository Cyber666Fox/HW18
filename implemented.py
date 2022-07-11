from service.movie import MoiveService
from service.genre import GenreService
from service.director import DirectorService
from setup_db import db
from dao.movie import MovieDAO
from dao.genre import GenreDAO
from dao.director import DirectorDAO


movie_dao = MovieDAO(db.session)
movie_service = MoiveService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
