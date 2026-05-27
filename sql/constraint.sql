ALTER TABLE transacoes_pix
ADD CONSTRAINT transacoes_pix_unique_key UNIQUE (
    data_transacao,
    pagador,
    receptor,
    regiao_pagador,
    regiao_receptor,
    idade_pagador,
    idade_receptor,
    forma_iniciacao,
    natureza_pix,
    finalidade
);