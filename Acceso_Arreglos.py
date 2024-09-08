import numpy as np

# Definimos las ciudades y los días de la semana
# Definimos las dimensiones
num_ciudades = 3  # Quito, Guayaquil, Cuenca
num_dias = 7      # Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo
num_semanas = 4   # Semana 1, Semana 2, Semana 3, Semana 4

# Creamos una matriz 3D con numpy
# Dimensiones: [ciudades, días, semanas]

temperaturas = np.zeros((num_ciudades, num_dias, num_semanas))
temp_variable = [
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 38}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 36}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 31}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 20}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 21}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 22}
        ]
    ]
]


# Imprimir la matriz
print("Temperaturas diarias en varias ciudades:")
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Llenamos la matriz con datos de temperatura (ejemplo aleatorio)
for i in range(len(ciudades)):
    for j in range(len(dias)):
        for k in range(num_semanas):
            # Asignamos una temperatura aleatoria entre 15 y 30 grados
            temperaturas[i][j][k] = np.random.uniform(15, 30)

# Imprimimos la matriz
for i, ciudad in enumerate(ciudades):
    print(f"Temperaturas en {ciudad}:")
    for k in range(num_semanas):
        print(f"Semana {k + 1}:")
        for j, dia in enumerate(dias):
            print(f"  {dia}: {temperaturas[i][j][k]:.2f} °C")
        print()