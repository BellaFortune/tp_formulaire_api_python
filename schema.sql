DROP TABLE IF EXISTS posts;

CREATE TABLE formulaires (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_du_bootcamp VARCHAR(30) NOT NULL,
    priorite_de_retour VARCHAR(30) NOT NULL,
    type_de_retour VARCHAR(30) NOT NULL,
    dates date NOT NULL,
    evaluation INTEGER NOT NULL,
    commentaire TEXT,
    piece_joites VARCHAR(250),
    droits_donnee  boolean
);