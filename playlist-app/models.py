"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    # ADD THE NECESSARY CODE HERE
    songs = relationship('PlaylistSong', back_populates='playlist')


class Song(db.Model):
    """Song."""
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    artist = Column(String)
    # ADD THE NECESSARY CODE HERE
    playlists = relationship('PlaylistSong', back_populates='song')

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    id = Column(Integer, primary_key=True, autoincrement=True)
    playlist_id = Column(Integer, ForeignKey('playlist.id'))
    song_id = Column(Integer, ForeignKey('song.id'))
    # ADD THE NECESSARY CODE HERE
    playlist = relationship('Playlist', back_populates='songs')
    song = relationship('Song', back_populates='playlists')

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)
   
