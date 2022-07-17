__author__ = 'Erik Telepovsky'



GENDER_MALE = 'male'
GENDER_FEMALE = 'female'

TipoCapacitacion = (
    ('tipo_1', 'Tipo 1'),
    ('tipo_2', 'Tipo 2'),
    ('tipo_3', 'Tipo 3')
)

RolCapacitacion = (
    ('rol_1', 'Rol 1'),
    ('rol_2', 'Rol 2'),
    ('rol_3', 'Rol 3')
)

ModalidadCapacitacion = (
    ('modalidad_1', 'Modalidad 1'),
    ('modalidad_2', 'Modalidad 2'),
    ('modalidad_3', 'Modalidad 3')
)


Years = (
    ('1976', '1976'),
    ('1977', '1977'),
    ('1978', '1978'),
    ('1979', '1979'),
    ('1980', '1980'),
    ('1981', '1981'),
    ('1982', '1982'),
    ('1983', '1983'),
    ('1984', '1984'),
    ('1985', '1985'),
    ('1986', '1986'),
    ('1987', '1987'),
    ('1988', '1988'),
    ('1989', '1989'),
    ('1990', '1990'),
    ('1991', '1991'),
    ('1992', '1992'),
    ('1993', '1993'),
    ('1994', '1994'),
    ('1995', '1995'),
    ('1996', '1996'),
    ('1997', '1997'),
    ('1998', '1998'),
    ('1999', '1999'),
    ('2000', '2000'),
    ('2001', '2001'),
    ('2002', '2002'),
    ('2003', '2003'),
    ('2004', '2004'),
    ('2005', '2005'),
    ('2006', '2006'),
    ('2007', '2007'),
    ('2008', '2008'),
    ('2009', '2009'),
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
    ('2015', '2015'),
    ('2016', '2016')
)


GENDER = (
    (GENDER_MALE, 'Malee'),
    (GENDER_FEMALE, 'Femalee')
)

NivelAutoria = (
    (1, '1er autor'),
    (2, '2do autor'),
    (3, '3er autor'),
    (4, '4to autor'),
    (5, '5to autor'),
    (6, 'Otro autor')
)

NivelMES = (
    (1, '1er nivel'),
    (2, '2do nivel'),
    (3, '3er nivel'),
    (4, '4to nivel'),
    (5, '5to nivel')
)

NivelEvento = (
    ("institucional", 'Institucional'),
    ('municipal', 'Municipal'),
    ('provincial', 'Provincial'),
    ('nacional', 'Nacional'),
    ('Regional', 'Regional'),
    ('internacional', 'Internacional'),
    ('otro', 'Otro')
)

TipoPublicacion = (
    ('libro', 'Libro'),
    ('articulo de revista', 'Articulo de Revista'),
    ('monografia', 'Monografia'),
    ('tesis', 'Tesis'),
    ('capitulo de libro', 'Capitulo de Libro'),
    ('conferencia', 'Conferencia'),
    ('otra', 'Otra')
)

NivelProyectoIDi = (
    ("facultad o area", 'Facultad o Area'),
    ('universitario', 'Universitario'),
    ('convocatoria ministerial', 'Convocatoria Ministerial'),
    ('convocatoria del extranjero', 'Convocatoria del Extranjero'),
    ('otras convocatorias nacionales', 'Otras convocatorias nacionales'),
    ('otro', 'Otro')
)

LineaCientificaProyectoIDi = (
    ('formacion del ingeniero en ciencias informaticas y tecnologia educativa', 'Formacion del Ingeniero en Ciencias Informaticas y Tecnologia Educativa'),
    ('inteligencia artificial', 'Inteligencia Artificial'),
    ('ingenieria y gestion de software', 'Ingenieria y Gestion de Software'),
    ('otra', 'Otra')
)

RolProyectoIDi = (
    ('trabajador', 'Trabajador'),
    ('jefe de grupo', 'Jefe de Grupo'),
    ('coordinador', 'Coordinador'),
    ('directivo', 'Directivo'),
    ('director', 'Director'),
)
CienciaObra = (
    ("sociales", 'Sociales'),
    ('juridicas', 'Juridicas'),
    ('tecnicas', 'Tecnicas'),
    ('informaticas', 'Informaticas'),
    ('pedagogicas', 'Pedagogicas'),
    ('de la educacion', 'de la Educacion'),
    ('otra', 'Otra')
)
TipoObra = (
    ('modelo', 'Modelo'),
    ('estrategia', 'Estrategia'),
    ('sistema', 'Sistema'),
    ('metodologia', 'Metodologia'),
    ('guia', 'Guia'),
    ('otro', 'Otro')
)
CantidadAutores = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6 o mas')
)
Tamanno = (
    ("grande", 'Grande'),
    ('mediano', 'Mediano'),
    ('pequeño', 'Pequeño')
)
LugarPremio = (
    ("1er Lugar", '1er Lugar'),
    ('2do Lugar', '2do Lugar'),
    ('3er Lugar', '3er Lugar'),
    ('4to Lugar', '4to Lugar'),
    ('5to Lugar', '5to Lugar'),
    ('mencion', 'Mencion'),
    ('otro premio', 'Otro premio')
)
CaracterPremio = (
    ("forum", 'FORUM'),
    ('jce', 'JCE'),
    ('SFF', 'SFF'),
    ('feria', 'Feria'),
    ('acc', 'ACC'),
    ('uic', 'UIC'),
    ('apc', 'APC'),
    ('otro', 'Otro')
)

FuenteEmpleoEstudiantes = (
    ('proyecto de investigacion', 'Proyecto de Investigacion'),
    ('proyecto de desarrollo de sotware', 'Proyecto de Desarrollo de Sotware'),
    ('proyecto de innovacion educativa', 'Proyecto de Innovacion Educativa'),
    ('tesis', 'Tesis'),
    ('otro', 'Otro')
)

CantidadEstudiantes = (
    ('1-5', '1-5'),
    ('6-10', '6-10'),
    ('11-15', '11-15'),
    ('16-20', '16-20'),
    ('21 o mas', '21 o mas')
)

NombreFuente = (
    ('Fuente 1', 'Fuente 1'),
    ('Fuente 2', 'Fuente 2'),
    ('Fuente 3', 'Fuente 3'),
    ('Fuente 4', 'Fuente 4'),
    ('Fuente 5', 'Fuente 5')
)

NombreObra = (
    ('Obra 1', 'Obra 1'),
    ('Obra 2', 'Obra 2'),
    ('Obra 3', 'Obra 3'),
    ('Obra 4', 'Obra 4'),
    ('Obra 5', 'Obra 5')
)

TiempoVisibilidad = (
    ('24 horas', '24 horas'),
    ('2-3 dias', '2-3 dias'),
    ('4-6 dias', '4-6 dias'),
    ('10 dias', '10 dias'),
    ('30 dias', '30 dias'),
    ('1 año', '1 año')
)

RangoTiempo = (
    ('Rango1', 'Rango1'),
    ('Rango2', 'Rango2')
)

CaracterNoticia = (
    ('urgente', 'Urgente'),
    ('ordinario', 'Ordinario')
)

NAMES = {
    GENDER_MALE: ['Andrew', 'Arthur', 'Ian', 'Eric', 'Leonard', 'Lukas', 'Matt', 'Peter', 'Vincent'],
    GENDER_FEMALE: ['Allison', 'Angela', 'Catherine', 'Elisabeth', 'Evangeline', 'Heidi', 'Katie', 'Lilly', 'Susan']
}

CONTINENT_NORTH_AMERICA = 'north_america'
CONTINENT_SOUTH_AMERICA = 'south_america'
CONTINENT_EUROPE = 'europe'
CONTINENT_ASIA = 'asia'
CONTINENT_AFRICA = 'africa'
CONTINENT_AUSTRALIA = 'australia'
CONTINENT_ANTARCTICA = 'antarctica'
CONTINENTS = (
    (CONTINENT_NORTH_AMERICA, 'North America'),
    (CONTINENT_SOUTH_AMERICA, 'South America'),
    (CONTINENT_EUROPE, 'Europe'),
    (CONTINENT_ASIA, 'Asia'),
    (CONTINENT_AFRICA, 'Africa'),
    (CONTINENT_AUSTRALIA, 'Australia'),
    (CONTINENT_ANTARCTICA, 'Antarctica')
)


# North America
COUNTRY_ALASKA = 'Alaska'
COUNTRY_CANADA = 'Canada'
COUNTRY_USA = 'USA'
COUNTRY_MEXICO = 'Mexico'

# South America
COUNTRY_COLOMBIA = 'Colombia'
COUNTRY_VENEZUELA = 'Venezuela'
COUNTRY_BRAZIL = 'Brazil'
COUNTRY_CHILE = 'Chile'
COUNTRY_URUGUAY = 'Uruguay'
COUNTRY_ARGENTINA = 'Argentina'

# Europe
COUNTRY_SLOVAKIA = 'Slovakia'
COUNTRY_SPAIN = 'Spain'
COUNTRY_BULGARIA = 'Bulgaria'
COUNTRY_PORTUGAL = 'Portugal'
COUNTRY_ITALY = 'Italy'
COUNTRY_UNITED_KINGDOM = 'United Kingdom'

# Asia
COUNTRY_CHINA = 'China'
COUNTRY_RUSSIA = 'Russia'
COUNTRY_JAPAN = 'Japan'
COUNTRY_INDIA = 'India'

# Africa
COUNTRY_ALGERIA = 'Algeria'
COUNTRY_EGYPT = 'Egypt'
COUNTRY_SUDAN = 'Sudan'
COUNTRY_ETHIOPIA = 'Ethiopia'
COUNTRY_SOMALIA = 'Somalia'
COUNTRY_MADAGASCAR = 'Madagascar'

# Australia
COUNTRY_WESTERN_AUSTRALIA = 'Western Australia'
COUNTRY_NORTHERN_TERRITORY = 'Northern Territory'
COUNTRY_SOUTH_AUSTRALIA = 'South Australia'
COUNTRY_QUEENSLAND = 'Queensland'
COUNTRY_NEW_SOUTH_WALES = 'New South Wales'
COUNTRY_VICTORIA = 'Victoria'
COUNTRY_AUSTRALIAN_CAPITAL_TERRITORY = 'Australian Capital Territory'
COUNTRY_TASMANIA = 'Tasmania'

# Antarctica
COUNTRY_SOUTH_ORKNEY_ISLANDS = 'South Orkney Islands'
COUNTRY_GRAHAM_LAND = 'Graham Land'
COUNTRY_MARIE_BYRD_LAND = 'Marie Byrd Land'
COUNTRY_QEEN_MAUD_LAND = 'Queen Maud Land'
COUNTRY_VICTORIA_LAND = 'Victoria Land'
COUNTRY_WILKES_LAND = 'Wilkes Land'

COUNTRIES = {
    CONTINENT_NORTH_AMERICA: [
        COUNTRY_ALASKA, COUNTRY_CANADA, COUNTRY_USA, COUNTRY_MEXICO
    ],
    CONTINENT_SOUTH_AMERICA: [
        COUNTRY_COLOMBIA, COUNTRY_VENEZUELA, COUNTRY_BRAZIL, COUNTRY_CHILE, COUNTRY_URUGUAY, COUNTRY_ARGENTINA
    ],
    CONTINENT_EUROPE: [
        COUNTRY_SLOVAKIA, COUNTRY_SPAIN, COUNTRY_BULGARIA, COUNTRY_PORTUGAL, COUNTRY_ITALY, COUNTRY_UNITED_KINGDOM
    ],
    CONTINENT_ASIA: [
        COUNTRY_CHINA, COUNTRY_RUSSIA, COUNTRY_JAPAN, COUNTRY_INDIA
    ],
    CONTINENT_AFRICA: [
        COUNTRY_ALGERIA, COUNTRY_EGYPT, COUNTRY_SUDAN, COUNTRY_ETHIOPIA, COUNTRY_SOMALIA, COUNTRY_MADAGASCAR
    ],
    CONTINENT_AUSTRALIA: [
        COUNTRY_WESTERN_AUSTRALIA, COUNTRY_NORTHERN_TERRITORY, COUNTRY_SOUTH_AUSTRALIA, COUNTRY_QUEENSLAND,
        COUNTRY_NEW_SOUTH_WALES, COUNTRY_VICTORIA, COUNTRY_TASMANIA, COUNTRY_AUSTRALIAN_CAPITAL_TERRITORY
    ],
    CONTINENT_ANTARCTICA: [
        COUNTRY_SOUTH_ORKNEY_ISLANDS, COUNTRY_GRAHAM_LAND, COUNTRY_MARIE_BYRD_LAND, COUNTRY_QEEN_MAUD_LAND,
        COUNTRY_VICTORIA_LAND, COUNTRY_WILKES_LAND
    ]
}

CITIES = {
    # North America
    COUNTRY_ALASKA: [
        'Anchorage', 'Fairbanks', 'Juneau', 'Sitka', 'Ketchikan', 'Wasilla', 'Kenai'
    ],
    COUNTRY_CANADA: [
        'Ottawa', 'Edmonton', 'Victoria', 'Winnipeg', 'Halifax', 'Toronto', 'Charlottetown', 'Quebec City'
    ],
    COUNTRY_USA: [
        'New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego'
    ],
    COUNTRY_MEXICO: [
        'Mexico City', 'Ecatepec', 'Guadalajara', 'Puebla', 'Leon', 'Juarez', 'Tijuana'
    ],

    # South America
    COUNTRY_COLOMBIA: [
        'Bogota', 'Medellin', 'Cali', 'Barranquilla', 'Cartagena'
    ],
    COUNTRY_VENEZUELA: [
        'Isla Raton', 'La Esmeralda', 'Maroa', 'Puerto Ayacucho', 'San Carlos de Rio Negro',
    ],
    COUNTRY_BRAZIL: [
        'Sao Paulo', 'Rio de Janeiro', 'Salvador', 'Fortaleza', 'Belo Horizonte'
    ],
    COUNTRY_CHILE: [
        'Puente Alto', 'Maipu', 'La Florida', 'Las Condes', 'San Bernardo'
    ],
    COUNTRY_URUGUAY: [
        'Montevideo', 'Salto', 'Ciudad de la Costa', 'Paysandu', 'Las Piedras', 'Rivera', 'Maldonado'
    ],
    COUNTRY_ARGENTINA: [
        'Buenos Aires', 'Cordoba', 'Rosario', 'Mendoza', 'La Plata'
    ],

    # Europe
    COUNTRY_SLOVAKIA: [
        'Bratislava', 'Kosice', 'Trebisov', 'Poprad', 'Zilina', 'Puchov', 'Banska Bystrica', 'Presov'
    ],
    COUNTRY_SPAIN: [
        'Madrid', 'Barcelona', 'Valencia', 'Seville', 'Zaragoza', 'Malaga', 'Murcia'
    ],
    COUNTRY_BULGARIA: [
        'Sofia', 'Plovdiv', 'Varna', 'Burgas', 'Ruse', 'Stara Zagora', 'Pleven', 'Sliven'
    ],
    COUNTRY_PORTUGAL: [
        'Lisbon', 'Porto', 'Vila Nova de Gaia', 'Amadora', 'Braga', 'Agualva-Cacem', 'Funchal'
    ],
    COUNTRY_ITALY: [
        'Rome', 'Milan', 'Naples', 'Turin', 'Palermo', 'Genoa', 'Bologna', 'Florence', 'Bari', 'Catania', 'Venice'
    ],
    COUNTRY_UNITED_KINGDOM: [
        'London', 'Wells', 'Ripon', 'Truro', 'Ely', 'Chichester', 'Worcester', 'Oxford'
    ],

    # Asia
    COUNTRY_CHINA: [
        'Beijing', 'Shanghai', 'Hong Kong', 'Jinjiang', 'Xiamen', 'Sihui'
    ],
    COUNTRY_RUSSIA: [
        'Moscow', 'Saint Petersburg', 'Novosibirsk', 'Yekaterinburg', 'Nizhny Novgorod', 'Samara', 'Omsk', 'Kazan'
    ],
    COUNTRY_JAPAN: [
        'Tokyo', 'Aichi', 'Akita', 'Chiba', 'Fukui', 'Fukushima', 'Hokkaido', 'Ishikawa', 'Kyoto', 'Osaka'
    ],
    COUNTRY_INDIA: [
        'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Jaipur'
    ],

    # Africa
    COUNTRY_ALGERIA: [
        'Alger', 'Oran', 'Constantine', 'Annaba', 'Blida', 'Batna', 'Djelfa'
    ],
    COUNTRY_EGYPT: [
        'Cairo', 'Alexandria', 'Giza', 'Shubra El-Kheima', 'Port Said', 'Suez', 'Luxor'
    ],
    COUNTRY_SUDAN: [
        'Omdurman', 'Khartoum', 'Khartoum Bahri', 'Nyala', 'Port Sudan', 'Kassala', 'Ubayyid', 'Kosti', 'Wad Madani'
    ],
    COUNTRY_ETHIOPIA: [
        'Addis Ababa', 'Dire Dawa', 'Mek\'ele', 'Adama', 'Gondar', 'Awasa', 'Bahir Dar', 'Jimma', 'Dessie'
    ],
    COUNTRY_SOMALIA: [
        'Mogadishu', 'Hargeisa', 'Bosaso', 'Galkayo', 'Berbera', 'Merca'
    ],
    COUNTRY_MADAGASCAR: [
        'Antananarivo', 'Toamasina', 'Antsirabe', 'Fianarantsoa', 'Mahajanga', 'Toliara', 'Antsiranana'
    ],

    # Australia
    COUNTRY_WESTERN_AUSTRALIA: [
        'Perth', 'Bunbury'
    ],
    COUNTRY_NORTHERN_TERRITORY: [
        'Darwin', 'Toowoomba'
    ],
    COUNTRY_SOUTH_AUSTRALIA: [
        'Adelaide'
    ],
    COUNTRY_QUEENSLAND: [
        'Brisbane', 'Gold Coast-Tweed', 'Sunshine Coast', 'Townsville', 'Cairns'
    ],
    COUNTRY_NEW_SOUTH_WALES: [
        'Sydney', 'Newcastle-Maitland', 'Wollongong', 'Albury-Wodonga'
    ],
    COUNTRY_VICTORIA: [
        'Melbourne', 'Geelong', 'Ballarat', 'Bendigo', 'Shepparton-Mooroopna'
    ],
    COUNTRY_AUSTRALIAN_CAPITAL_TERRITORY: [
        'Canberra-Queanbeyan',
    ],
    COUNTRY_TASMANIA: [
        'Hobart', 'Launceston'
    ],

    # Antarctica
    COUNTRY_SOUTH_ORKNEY_ISLANDS: [

    ],
    COUNTRY_GRAHAM_LAND: [

    ],
    COUNTRY_MARIE_BYRD_LAND: [

    ],
    COUNTRY_QEEN_MAUD_LAND: [

    ],
    COUNTRY_VICTORIA_LAND: [

    ],
    COUNTRY_WILKES_LAND: [

    ],
}
