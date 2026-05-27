CREATE TABLE transacoes_pix (
    id SERIAL PRIMARY KEY,
    data_transacao DATE NOT NULL,
    pagador VARCHAR(2) NOT NULL,
    receptor VARCHAR(2) NOT NULL,
    regiao_pagador VARCHAR(15) NOT NULL,
    regiao_receptor VARCHAR(15) NOT NULL,
    idade_pagador VARCHAR(20) NOT NULL,
    idade_receptor VARCHAR(20) NOT NULL,
    forma_iniciacao VARCHAR(15) NOT NULL,
    natureza_pix VARCHAR(3) NOT NULL,
    finalidade VARCHAR(30) NOT NULL,
    valor_pix NUMERIC(18,2) NOT NULL,
    quantidade_pix INTEGER NOT NULL,
    criado_em TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);