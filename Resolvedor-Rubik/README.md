este proyecto busca resolver cualquier cubo de rubik 3x3, buscando el camino optimo usando programacion dinamica.
se usa una orientacion fija del cubo y solo se guarda las esquinas y aristas de cada estado

Caras:
frontal: roja (r)
derecha: azul (b)
superior: blanca (w)
izquierda: verde (g)
inferior: amarilla (y)
trasera: naranja (o)

cubo = {
        "esquinas_pos": [0,1,2,3,4,5,6,7],
        "esquinas_ori": [0,0,0,0,0,0,0,0],
        "aristas_pos": [0,1,2,3,4,5,6,7,8,9,10,11],
        "aristas_ori": [0,0,0,0,0,0,0,0,0,0,0,0]
    }

esquinas: [ryb,rgy,rwg,rbw, oby,oyg,ogw,owb]

aristas: [ry,rg,rw,rb, gy,gw,wb,by, oy,og,ow,ob]
