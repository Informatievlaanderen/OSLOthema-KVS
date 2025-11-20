# Swagger

In [openapi.yml](./openapi.yml) is de Swagger gedefineerd voor de uitwisseling van de data volgens het [OSLO implementatiemodel](https://data.vlaanderen.be/doc/implementatiemodel/klantvolgsysteem1) voor Release 1.

Voor het opvragen van de codelijsten is er ook een aparte Swagger voorzien voor het genereren van een client SDK, maar deze is geen onderdeel van het datamodel, dit is puur als ondersteuning voor de ontwikkelaars: [SKOS/openapi.yml](./SKOS/openapi.yml). Een betere optie voor het lezen en gebruiken van de data is door gebruik te maken van SPARQL queries op de data, hierdoor kan je allerlei vragen stellen aan de data zonder dat je beperkt bent in de vorm van de API zoals bij Swagger. Een aantal voorbeelden kan je hieronder vinden inclusief een playground om ze uit te proberen tegen de mocking data.

# SPARQL help

- Veel voorbeelden van SPARQL queries: [https://en.wikibooks.org/wiki/SPARQL](https://en.wikibooks.org/wiki/SPARQL)
- Comunica, een online SPARQL executor die bronnen op het Web kan raadplegen: [https://query.comunica.dev](https://query.comunica.dev)
- SPARQL specificatie van W3C: [https://www.w3.org/TR/sparql11-query/](https://www.w3.org/TR/sparql11-query/)

## SPARQL voorbeelden per klasse

## Adres

**Demo met mocking data**: [Comunica.dev](https://query.comunica.dev/#datasources=https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fswagger%2FR1%2Frelease1.jsonld&query=PREFIX%20locn%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Flocn%23%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20adres%3A%20%3Chttps%3A%2F%2Fdata.vlaanderen.be%2Fns%2Fadres%23%3E%0A%0A%23%20Each%20variable%20besides%20type%20and%20id%20are%20fully%20optional%20as%20required%20by%20VDAB.%0ASELECT%20%3Fid%20%3Ftype%20%3FStraatnaam%20%3FHuisnummer%20%3FBusnummer%20%3FPostcode%20%3FGemeentenaam%20%3FLand%20%7B%0A%20%20%3Fid%20rdf%3Atype%20locn%3AAddress%20.%0A%20%20%3Fid%20rdf%3Atype%20%3Ftype%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20locn%3Athoroughfare%20%3FStraatnaam%20%7D%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20adres%3Ahuisnummer%20%3FHuisnummer%20%7D%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20adres%3Abusnummer%20%3FBusnummer%20%7D%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20locn%3ApostCode%20%3FPostcode%20%7D%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20adres%3Agemeentenaam%20%3FGemeentenaam%20%7D%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20adres%3Aland%20%3FLand%20%7D%20.%0A%7D)

**Query**
```
PREFIX locn: <http://www.w3.org/ns/locn#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX adres: <https://data.vlaanderen.be/ns/adres#>

# Each variable besides type and id are fully optional as required by VDAB.
SELECT ?id ?type ?Straatnaam ?Huisnummer ?Busnummer ?Postcode ?Gemeentenaam ?Land {
  ?id rdf:type locn:Address .
  ?id rdf:type ?type .
  OPTIONAL { ?id locn:thoroughfare ?Straatnaam } .
  OPTIONAL { ?id adres:huisnummer ?Huisnummer } .
  OPTIONAL { ?id adres:busnummer ?Busnummer } .
  OPTIONAL { ?id locn:postCode ?Postcode } .
  OPTIONAL { ?id adres:gemeentenaam ?Gemeentenaam } .
  OPTIONAL { ?id adres:land ?Land } .
}
```

## Identificator

**Demo met mocking data**: [Comunica.dev](https://query.comunica.dev/#datasources=https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fswagger%2FR1%2Frelease1.jsonld&query=PREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0APREFIX%20adms%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fadms%23%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0A%0A%23%20Each%20variable%20besides%20type%20and%20id%20are%20fully%20optional%20as%20required%20by%20VDAB.%0ASELECT%20%3Fid%20%3Ftype%20%3FValue%20%3FToegekendDoor%20%7B%0A%20%20%3Fid%20rdf%3Atype%20adms%3AIdentifier%20.%0A%20%20%3Fid%20rdf%3Atype%20%3Ftype%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20skos%3Anotation%20%3FValue%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fid%20adms%3AschemaAgency%20%3FToegekendDoor%20%7D%0A%7D)

**Query**
```
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX adms: <http://www.w3.org/ns/adms#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

# Each variable besides type and id are fully optional as required by VDAB.
SELECT ?id ?type ?Value ?ToegekendDoor {
  ?id rdf:type adms:Identifier .
  ?id rdf:type ?type .
  OPTIONAL { ?id skos:notation ?Value }
  OPTIONAL { ?id adms:schemaAgency ?ToegekendDoor }
}
```

## Contactpunt

**Demo met mocking data**: [Comunica.dev](https://query.comunica.dev/#datasources=https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fswagger%2FR1%2Frelease1.jsonld&query=PREFIX%20locn%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Flocn%23%3E%0APREFIX%20schema%3A%20%3Chttps%3A%2F%2Fschema.org%2F%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0A%0A%23%20Each%20variable%20besides%20type%20and%20id%20are%20fully%20optional%20as%20required%20by%20VDAB.%0ASELECT%20%3Fid%20%3Ftype%20%3FEmail%20%3FTelefoon%20%3FAdres%20%7B%0A%20%20%3Fid%20rdf%3Atype%20schema%3AContactPoint%20.%0A%20%20%3Fid%20rdf%3Atype%20%3Ftype%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20schema%3Aemail%20%3FEmail%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fid%20schema%3Atelephone%20%3FTelefoon%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fid%20locn%3Aaddress%20%3FAdres%20%7D%0A%7D)

**Query**
```
PREFIX locn: <http://www.w3.org/ns/locn#>
PREFIX schema: <https://schema.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

# Each variable besides type and id are fully optional as required by VDAB.
SELECT ?id ?type ?Email ?Telefoon ?Adres {
  ?id rdf:type schema:ContactPoint .
  ?id rdf:type ?type .
  OPTIONAL { ?id schema:email ?Email }
  OPTIONAL { ?id schema:telephone ?Telefoon }
  OPTIONAL { ?id locn:address ?Adres }
}
```

## Werkvoorkeuren

**Demo met mocking data**: [Comunica.dev](https://query.comunica.dev/#datasources=https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fswagger%2FR1%2Frelease1.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FDeeltrajecttype%2FOpleiding.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FVoorkeurtype%2FGewenstBeroep.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FVoorkeurtype%2FTeVerkennenBeroep.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FVoorkeurtype%2FTeLerenBeroep.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FVoorkeurtype%2FUitgeslotenBeroep.jsonld&query=PREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0APREFIX%20dcterms%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0APREFIX%20kvs1%3A%20%3Chttps%3A%2F%2Fdata.vlaanderen.be%2Fns%2Fklantvolgsysteem1%2F%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20dv-conceptscheme%3A%20%3Chttps%3A%2F%2Fdata.vlaanderen.be%2Fid%2Fconceptscheme%2F%3E%0A%0A%23%20Each%20variable%20besides%20type%20and%20id%20are%20fully%20optional%20as%20required%20by%20VDAB.%0ASELECT%20%3Fid%20%3Ftype%20%3FberoepstoestandId%20%3FvoorkeurId%20%3Fnaam%20%3FvoorkeurLabel%20%3FvoorkeurDefinitie%20%7B%0A%20%20%23%20Get%20all%20Werkvoorkeuren%20objects%0A%20%20%3Fid%20rdf%3Atype%20kvs1%3AWerkvoorkeuren%20.%0A%20%20%3Fid%20rdf%3Atype%20%3Ftype%20.%0A%20%20%23%20Werkvoorkeuren%20have%20an%20attribute%20beroep%20pointing%20to%20Beroeptoestand%20classes%0A%20%20OPTIONAL%20%7B%20%0A%20%20%20%20%3Fid%20kvs1%3Aberoep%20%3FberoepstoestandId%20.%0A%20%20%20%20%7B%0A%20%20%20%20%20%23%20Get%20all%20Beroeptoestand%20objects%20and%20match%20them%20by%20blanknode%20ID%20to%20the%20Werkvoorkeuren.%0A%20%20%20%20%20SELECT%20%3FberoepstoestandId%20%3Fnaam%20%3FvoorkeurId%20%3FvoorkeurLabel%20%3FvoorkeurDefinitie%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%3FberoepstoestandId%20rdf%3Atype%20kvs1%3ABeroepstoestand%20.%0A%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FberoepstoestandId%20dcterms%3Atitle%20%3Fnaam%20%7D%20.%0A%20%20%20%20%20%20%20%20%23%20Label%20and%20definition%20of%20each%20enumeration%20item%20is%20defined%20in%20SKOS%20Concept%20objects%2C%20get%20them%20and%20list%20their%20properties.%0A%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FberoepstoestandId%20kvs1%3Avoorkeur%20%3FvoorkeurId%20.%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20SELECT%20%3FvoorkeurId%20%3FvoorkeurLabel%20%3FvoorkeurDefinitie%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3FvoorkeurId%20rdf%3Atype%20skos%3AConcept%20.%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3FvoorkeurId%20skos%3Ainscheme%20dv-conceptscheme%3AVoorkeurType%20.%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3FvoorkeurId%20skos%3AprefLabel%20%3FvoorkeurLabel%20.%0A%20%20%20%20%20%20%20%20%09%20%20%3FvoorkeurId%20skos%3Adefinition%20%3FvoorkeurDefinitie%20.%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A)

**Query**
```
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX kvs1: <https://data.vlaanderen.be/ns/klantvolgsysteem1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dv-conceptscheme: <https://data.vlaanderen.be/id/conceptscheme/>

# Each variable besides type and id are fully optional as required by VDAB.
SELECT ?id ?type ?beroepstoestandId ?voorkeurId ?naam ?voorkeurLabel ?voorkeurDefinitie {
  # Get all Werkvoorkeuren objects
  ?id rdf:type kvs1:Werkvoorkeuren .
  ?id rdf:type ?type .
  # Werkvoorkeuren have an attribute beroep pointing to Beroeptoestand classes
  OPTIONAL {
    ?id kvs1:beroep ?beroepstoestandId .
    {
     # Get all Beroeptoestand objects and match them by blanknode ID to the Werkvoorkeuren.
     SELECT ?beroepstoestandId ?naam ?voorkeurId ?voorkeurLabel ?voorkeurDefinitie WHERE {
        ?beroepstoestandId rdf:type kvs1:Beroepstoestand .
        OPTIONAL { ?beroepstoestandId dcterms:title ?naam } .
        # Label and definition of each enumeration item is defined in SKOS Concept objects, get them and list their properties.
        OPTIONAL { ?beroepstoestandId kvs1:voorkeur ?voorkeurId .
          {
            SELECT ?voorkeurId ?voorkeurLabel ?voorkeurDefinitie {
              ?voorkeurId rdf:type skos:Concept .
              ?voorkeurId skos:inscheme dv-conceptscheme:VoorkeurType .
              ?voorkeurId skos:prefLabel ?voorkeurLabel .
              ?voorkeurId skos:definition ?voorkeurDefinitie .
            }
          }
        }
      }
    }
  }
}
```

## Publieke Dienstverlening

**Demo met mocking data**: [Comunica.dev](https://query.comunica.dev/#datasources=https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fswagger%2FR1%2Frelease1.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FFinaliteitType%2FSociaalOnderzoek.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FFinaliteitType%2FGPMI.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FPubliekeDienstverleningType%2FActiveringNaarWerk.jsonld&query=PREFIX%20cpsv%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fvocab%2Fcpsv%23%3E%0APREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0APREFIX%20dcterms%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0APREFIX%20kvs1%3A%20%3Chttps%3A%2F%2Fdata.vlaanderen.be%2Fns%2Fklantvolgsysteem1%2F%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20dv-conceptscheme%3A%20%3Chttps%3A%2F%2Fdata.vlaanderen.be%2Fid%2Fconceptscheme%2F%3E%20%0A%0ASELECT%20%3Fid%20%3Ftype%20%3FpubliekeDienstverleningType%20%3FdienstverleningLabel%20%3FdienstverleningDefinitie%20%3Fnaam%20%3FfinaliteitId%20%3FfinaliteitLabel%20%3FfinaliteitDefinitie%20%3FwerkvoorkeurenId%20%3FtrajectId%20%7B%0A%20%3Fid%20rdf%3Atype%20cpsv%3APublicService.%0A%20%3Fid%20rdf%3Atype%20%3Ftype.%0A%20OPTIONAL%20%7B%20%3Fid%20dcterms%3Atitle%20%3Fnaam%20%7D.%0A%20OPTIONAL%20%7B%20%0A%20%20%20%20%3Fid%20kvs1%3Afinaliteit%20%3FfinaliteitId%20.%0A%20%20%20%20%7B%0A%20%20%20%20%20%20SELECT%20%3FfinaliteitId%20%3FfinaliteitLabel%20%3FfinaliteitDefinitie%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%3FfinaliteitId%20rdf%3Atype%20skos%3AConcept%20.%0A%20%20%20%20%20%20%20%20%3FfinaliteitId%20skos%3Ainscheme%20dv-conceptscheme%3AFinaliteitType%20.%0A%20%20%20%20%20%20%20%20%3FfinaliteitId%20skos%3AprefLabel%20%3FfinaliteitLabel%20.%0A%20%20%20%20%20%20%20%20%3FfinaliteitId%20skos%3Adefinition%20%3FfinaliteitDefinitie%20.%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D.%0A%20%20OPTIONAL%20%7B%20%0A%20%20%20%20%3Fid%20dcterms%3Atype%20%3FpubliekeDienstverleningType%20.%0A%20%20%20%20%7B%0A%20%20%20%20%20%20SELECT%20%3FpubliekeDienstverleningTypeId%20%3FdienstverleningLabel%20%3FdienstverleningDefinitie%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%3FpubliekeDienstverleningTypeId%20rdf%3Atype%20skos%3AConcept%20.%0A%20%20%20%20%20%20%20%20%3FpubliekeDienstverleningTypeId%20skos%3Ainscheme%20dv-conceptscheme%3APubliekeDienstverleningType%20.%0A%20%20%20%20%20%20%20%20%3FpubliekeDienstverleningTypeId%20skos%3AprefLabel%20%3FdienstverleningLabel%20.%0A%20%20%20%20%20%20%20%20%3FpubliekeDienstverleningTypeId%20skos%3Adefinition%20%3FdienstverleningDefinitie%20.%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D.%0A%20%20OPTIONAL%20%7B%20%3Fid%20cpsv%3AhasInput%20%3FwerkvoorkeurenId%20%7D.%0A%20%20OPTIONAL%20%7B%20%3Fid%20cpsv%3Aproduces%20%3FtrajectId%20%7D.%0A%7D)

**Query**
```
PREFIX cpsv: <http://purl.org/vocab/cpsv#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX kvs1: <https://data.vlaanderen.be/ns/klantvolgsysteem1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dv-conceptscheme: <https://data.vlaanderen.be/id/conceptscheme/>

SELECT ?id ?type ?publiekeDienstverleningType ?dienstverleningLabel ?dienstverleningDefinitie ?naam ?finaliteitId ?finaliteitLabel ?finaliteitDefinitie ?werkvoorkeurenId ?trajectId {
 ?id rdf:type cpsv:PublicService.
 ?id rdf:type ?type.
 OPTIONAL { ?id dcterms:title ?naam }.
 OPTIONAL {
    ?id kvs1:finaliteit ?finaliteitId .
    {
      SELECT ?finaliteitId ?finaliteitLabel ?finaliteitDefinitie WHERE {
        ?finaliteitId rdf:type skos:Concept .
        ?finaliteitId skos:inscheme dv-conceptscheme:FinaliteitType .
        ?finaliteitId skos:prefLabel ?finaliteitLabel .
        ?finaliteitId skos:definition ?finaliteitDefinitie .
      }
    }
  }.
  OPTIONAL {
    ?id dcterms:type ?publiekeDienstverleningType .
    {
      SELECT ?publiekeDienstverleningTypeId ?dienstverleningLabel ?dienstverleningDefinitie WHERE {
        ?publiekeDienstverleningTypeId rdf:type skos:Concept .
        ?publiekeDienstverleningTypeId skos:inscheme dv-conceptscheme:PubliekeDienstverleningType .
        ?publiekeDienstverleningTypeId skos:prefLabel ?dienstverleningLabel .
        ?publiekeDienstverleningTypeId skos:definition ?dienstverleningDefinitie .
      }
    }
  }.
  OPTIONAL { ?id cpsv:hasInput ?werkvoorkeurenId }.
  OPTIONAL { ?id cpsv:produces ?trajectId }.
}
```

## Participant

**Demo met mocking data**: [Comunica.dev](https://query.comunica.dev/#datasources=https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fswagger%2FR1%2Frelease1.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FParticipatietype%2FBegeleider.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FParticipatietype%2FWerkzoekende.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FParticipatietype%2FContactpersoon.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FParticipatietype%2FBemiddelaar.jsonld&query=PREFIX%20locn%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Flocn%23%3E%0APREFIX%20schema%3A%20%3Chttps%3A%2F%2Fschema.org%2F%3E%0APREFIX%20adms%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fadms%23%3E%0APREFIX%20foaf%3A%20%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E%0APREFIX%20person%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fperson%23%3E%0APREFIX%20regorg%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fregorg%23%3E%0APREFIX%20persoon%3A%20%3Chttps%3A%2F%2Fdata.vlaanderen.be%2Fns%2Fpersoon%23%3E%0APREFIX%20m8g%3A%20%3Chttp%3A%2F%2Fdata.europa.eu%2Fm8g%2F%3E%0APREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0APREFIX%20dcterms%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0APREFIX%20kvs1%3A%20%3Chttps%3A%2F%2Fdata.vlaanderen.be%2Fns%2Fklantvolgsysteem1%2F%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20dv-conceptscheme%3A%20%3Chttps%3A%2F%2Fdata.vlaanderen.be%2Fid%2Fconceptscheme%2F%3E%0A%0A%23%20Each%20variable%20besides%20type%20and%20id%20are%20fully%20optional%20as%20required%20by%20VDAB.%0ASELECT%20%3Fid%20%3Ftype%20%3FrolId%20%3FrolLabel%20%3FrolDefinitie%20%3Fparticipant%20%3FidentificatorValue%20%3FidentificatorUitgereiktDoor%20%3Fvoornaam%20%3Fachternaam%20%3Fvoorkeursnaam%20%3FcontactInfo%20%3Fadres%20%3Ftelefoon%20%3Femail%20WHERE%20%7B%0A%20%20%23%20Get%20all%20Participatie%20objects%0A%20%20%3Fid%20rdf%3Atype%20m8g%3AParticipation%20.%0A%20%20%3Fid%20rdf%3Atype%20%3Ftype%20.%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fid%20m8g%3AhasParticipant%20%3Fparticipant%20%0A%20%20%20%20%23%20Geregistreerd%20Persoon%0A%20%20%20%20%7B%0A%20%20%20%20%20%20SELECT%20%3Fparticipant%20%3FidentificatorValue%20%3FidentificatorUitgereiktDoor%20%3FcontactInfo%20%3Femail%20%3Ftelefoon%20%3Fadres%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%3Fparticipant%20rdf%3Atype%20persoon%3AGeregistreerdPersoon%20.%0A%20%20%20%20%20%20%20%20%3Fparticipant%20persoon%3Aregistratie%20%3Fidentificator%20.%0A%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20SELECT%20%3Fidentificator%20%3FidentificatorValue%20%3FidentificatorUitgereiktDoor%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Fidentificator%20rdf%3Atype%20adms%3AIdentifier%20.%0A%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fidentificator%20skos%3Anotation%20%3FidentificatorValue%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fidentificator%20adms%3AschemaAgency%20%3FidentificatorUitgereiktDoor%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20OPTIONAL%20%7B%0A%20%20%20%20%20%20%20%20%20%20%3Fparticipant%20schema%3AcontactPoint%20%3FcontactInfo.%0A%20%20%20%20%20%20%20%20%20%20%3FcontactInfo%20rdf%3Atype%20schema%3AContactPoint%20.%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20SELECT%20%3FcontactInfo%20%3Femail%20%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FcontactInfo%20schema%3Aemail%20%3Femail%20%7D.%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20SELECT%20%3Ftelefoon%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FcontactInfo%20schema%3Atelephone%20%3Ftelefoon%20%7D.%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20SELECT%20%3Fadres%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FcontactInfo%20locn%3Aaddress%20%3Fadres%20%7D.%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%20%0A%20%20%20%20UNION%20%0A%20%20%20%20%23%20Persoon%0A%20%20%20%20%7B%0A%20%20%20%20%20%20SELECT%20%3Fparticipant%20%3Fachternaam%20%3Fvoornaam%20%3FcontactInfo%20%3Femail%20%3Ftelefoon%20%3Fadres%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%3Fparticipant%20rdf%3Atype%20person%3APerson%20.%0A%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fparticipant%20foaf%3AgivenName%20%3Fvoornaam%20%7D%20.%0A%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%20%3Fparticipant%20foaf%3AfamilyName%20%3Fachternaam%20%7D%20.%0A%20%20%20%20%20%20%20%20OPTIONAL%20%7B%0A%20%20%20%20%20%20%20%20%20%20%3Fparticipant%20schema%3AcontactPoint%20%3FcontactInfo.%0A%20%20%20%20%20%20%20%20%20%20%3FcontactInfo%20rdf%3Atype%20schema%3AContactPoint%20.%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20SELECT%20%3FcontactInfo%20%3Femail%20%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FcontactInfo%20schema%3Aemail%20%3Femail%20%7D.%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20SELECT%20%3Ftelefoon%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FcontactInfo%20schema%3Atelephone%20%3Ftelefoon%20%7D.%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20SELECT%20%3Fadres%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FcontactInfo%20locn%3Aaddress%20%3Fadres%20%7D.%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20UNION%0A%20%20%20%20%23%20GeregistreerdeOrganisatie%0A%20%20%20%20%7B%0A%20%20%20%20%20%20SELECT%20%3Fparticipant%20%3FidentificatorValue%20%3FidentificatorUitgereiktDoor%20%3Fvoorkeursnaam%20%3FcontactInfo%20%3Femail%20%3Ftelefoon%20%3Fadres%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%3Fparticipant%20rdf%3Atype%20regorg%3ARegisteredOrganisation%20.%0A%20%20%20%20%20%20%20%20%3Fparticipant%20regorg%3Aregistration%20%3Fidentificator%20.%0A%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20SELECT%20%3Fidentificator%20%3FidentificatorValue%20%3FidentificatorUitgereiktDoor%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Fidentificator%20rdf%3Atype%20adms%3AIdentifier%20.%0A%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fidentificator%20skos%3Anotation%20%3FidentificatorValue%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fidentificator%20adms%3AschemaAgency%20%3FidentificatorUitgereiktDoor%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fparticipant%20skos%3AprefLabel%20%3Fvoorkeursnaam%20%7D%20.%0A%20%20%20%20%20%20%20%20OPTIONAL%20%7B%0A%20%20%20%20%20%20%20%20%20%20%3Fparticipant%20schema%3AcontactPoint%20%3FcontactInfo.%0A%20%20%20%20%20%20%20%20%20%20%3FcontactInfo%20rdf%3Atype%20schema%3AContactPoint%20.%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20SELECT%20%3FcontactInfo%20%3Femail%20%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FcontactInfo%20schema%3Aemail%20%3Femail%20%7D.%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20SELECT%20%3Ftelefoon%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FcontactInfo%20schema%3Atelephone%20%3Ftelefoon%20%7D.%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20SELECT%20%3Fadres%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FcontactInfo%20locn%3Aaddress%20%3Fadres%20%7D.%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%20%20UNION%0A%20%20%20%20%23%20PubliekeOrganisatie%0A%20%20%20%20%7B%0A%20%20%20%20%20%20SELECT%20%3Fparticipant%20%3FidentificatorValue%20%3FidentificatorUitgereiktDoor%20%3Fvoorkeursnaam%20%3FcontactInfo%20%3Femail%20%3Ftelefoon%20%3Fadres%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%3Fparticipant%20rdf%3Atype%20m8g%3APublicOrganisation%20.%0A%20%20%20%20%20%20%20%20%3Fparticipant%20adms%3Aidentifier%20%3Fidentificator%20.%0A%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20SELECT%20%3Fidentificator%20%3FidentificatorValue%20%3FidentificatorUitgereiktDoor%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Fidentificator%20rdf%3Atype%20adms%3AIdentifier%20.%0A%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fidentificator%20skos%3Anotation%20%3FidentificatorValue%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fidentificator%20adms%3AschemaAgency%20%3FidentificatorUitgereiktDoor%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fparticipant%20skos%3AprefLabel%20%3Fvoorkeursnaam%20%7D%20.%0A%20%20%20%20%20%20%20%20OPTIONAL%20%7B%0A%20%20%20%20%20%20%20%20%20%20%3Fparticipant%20schema%3AcontactPoint%20%3FcontactInfo.%0A%20%20%20%20%20%20%20%20%20%20%3FcontactInfo%20rdf%3Atype%20schema%3AContactPoint%20.%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20SELECT%20%3FcontactInfo%20%3Femail%20%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FcontactInfo%20schema%3Aemail%20%3Femail%20%7D.%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20SELECT%20%3Ftelefoon%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FcontactInfo%20schema%3Atelephone%20%3Ftelefoon%20%7D.%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20SELECT%20%3Fadres%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3FcontactInfo%20locn%3Aaddress%20%3Fadres%20%7D.%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D.%0A%20%20OPTIONAL%20%7B%20%0A%20%20%20%20%3Fid%20m8g%3Arole%20%3FrolId%20.%0A%20%20%20%20%7B%0A%20%20%20%09%20%20SELECT%20%3FrolId%20%3FrolLabel%20%3FrolDefinitie%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%3FrolId%20rdf%3Atype%20skos%3AConcept%20.%0A%20%20%20%20%20%20%20%20%3FrolId%20skos%3Ainscheme%20dv-conceptscheme%3AParticipatietype%20.%0A%20%20%20%20%20%20%20%20%3FrolId%20skos%3AprefLabel%20%3FrolLabel%20.%0A%20%20%20%20%20%20%20%20%3FrolId%20skos%3Adefinition%20%3FrolDefinitie%20.%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D%0A)

**Query**
```
PREFIX locn: <http://www.w3.org/ns/locn#>
PREFIX schema: <https://schema.org/>
PREFIX adms: <http://www.w3.org/ns/adms#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX person: <http://www.w3.org/ns/person#>
PREFIX regorg: <http://www.w3.org/ns/regorg#>
PREFIX persoon: <https://data.vlaanderen.be/ns/persoon#>
PREFIX m8g: <http://data.europa.eu/m8g/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX kvs1: <https://data.vlaanderen.be/ns/klantvolgsysteem1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dv-conceptscheme: <https://data.vlaanderen.be/id/conceptscheme/>

# Each variable besides type and id are fully optional as required by VDAB.
SELECT ?id ?type ?rolId ?rolLabel ?rolDefinitie ?participant ?identificatorValue ?identificatorUitgereiktDoor ?voornaam ?achternaam ?voorkeursnaam ?contactInfo ?adres ?telefoon ?email WHERE {
  # Get all Participatie objects
  ?id rdf:type m8g:Participation .
  ?id rdf:type ?type .
  OPTIONAL {
    ?id m8g:hasParticipant ?participant
    # Geregistreerd Persoon
    {
      SELECT ?participant ?identificatorValue ?identificatorUitgereiktDoor ?contactInfo ?email ?telefoon ?adres WHERE {
        ?participant rdf:type persoon:GeregistreerdPersoon .
        ?participant persoon:registratie ?identificator .
        {
          SELECT ?identificator ?identificatorValue ?identificatorUitgereiktDoor {
            ?identificator rdf:type adms:Identifier .
            OPTIONAL { ?identificator skos:notation ?identificatorValue }
            OPTIONAL { ?identificator adms:schemaAgency ?identificatorUitgereiktDoor }
          }
        }
        OPTIONAL {
          ?participant schema:contactPoint ?contactInfo.
          ?contactInfo rdf:type schema:ContactPoint .
          {
            SELECT ?contactInfo ?email  WHERE {
              OPTIONAL { ?contactInfo schema:email ?email }.
            }
          }
          {
            SELECT ?telefoon WHERE {
              OPTIONAL { ?contactInfo schema:telephone ?telefoon }.
            }
          }
          {
            SELECT ?adres WHERE {
              OPTIONAL { ?contactInfo locn:address ?adres }.
            }
          }
        }
      }
    }
    UNION
    # Persoon
    {
      SELECT ?participant ?achternaam ?voornaam ?contactInfo ?email ?telefoon ?adres WHERE {
        ?participant rdf:type person:Person .
        OPTIONAL { ?participant foaf:givenName ?voornaam } .
        OPTIONAL {  ?participant foaf:familyName ?achternaam } .
        OPTIONAL {
          ?participant schema:contactPoint ?contactInfo.
          ?contactInfo rdf:type schema:ContactPoint .
          {
            SELECT ?contactInfo ?email  WHERE {
              OPTIONAL { ?contactInfo schema:email ?email }.
            }
          }
          {
            SELECT ?telefoon WHERE {
              OPTIONAL { ?contactInfo schema:telephone ?telefoon }.
            }
          }
          {
            SELECT ?adres WHERE {
              OPTIONAL { ?contactInfo locn:address ?adres }.
            }
          }
        }
      }
    }
    UNION
    # GeregistreerdeOrganisatie
    {
      SELECT ?participant ?identificatorValue ?identificatorUitgereiktDoor ?voorkeursnaam ?contactInfo ?email ?telefoon ?adres WHERE {
        ?participant rdf:type regorg:RegisteredOrganisation .
        ?participant regorg:registration ?identificator .
        {
          SELECT ?identificator ?identificatorValue ?identificatorUitgereiktDoor {
            ?identificator rdf:type adms:Identifier .
            OPTIONAL { ?identificator skos:notation ?identificatorValue }
            OPTIONAL { ?identificator adms:schemaAgency ?identificatorUitgereiktDoor }
          }
        }
        OPTIONAL { ?participant skos:prefLabel ?voorkeursnaam } .
        OPTIONAL {
          ?participant schema:contactPoint ?contactInfo.
          ?contactInfo rdf:type schema:ContactPoint .
          {
            SELECT ?contactInfo ?email  WHERE {
              OPTIONAL { ?contactInfo schema:email ?email }.
            }
          }
          {
            SELECT ?telefoon WHERE {
              OPTIONAL { ?contactInfo schema:telephone ?telefoon }.
            }
          }
          {
            SELECT ?adres WHERE {
              OPTIONAL { ?contactInfo locn:address ?adres }.
            }
          }
        }
      }
    }
    UNION
    # PubliekeOrganisatie
    {
      SELECT ?participant ?identificatorValue ?identificatorUitgereiktDoor ?voorkeursnaam ?contactInfo ?email ?telefoon ?adres WHERE {
        ?participant rdf:type m8g:PublicOrganisation .
        ?participant adms:identifier ?identificator .
        {
          SELECT ?identificator ?identificatorValue ?identificatorUitgereiktDoor {
            ?identificator rdf:type adms:Identifier .
            OPTIONAL { ?identificator skos:notation ?identificatorValue }
            OPTIONAL { ?identificator adms:schemaAgency ?identificatorUitgereiktDoor }
          }
        }
        OPTIONAL { ?participant skos:prefLabel ?voorkeursnaam } .
        OPTIONAL {
          ?participant schema:contactPoint ?contactInfo.
          ?contactInfo rdf:type schema:ContactPoint .
          {
            SELECT ?contactInfo ?email  WHERE {
              OPTIONAL { ?contactInfo schema:email ?email }.
            }
          }
          {
            SELECT ?telefoon WHERE {
              OPTIONAL { ?contactInfo schema:telephone ?telefoon }.
            }
          }
          {
            SELECT ?adres WHERE {
              OPTIONAL { ?contactInfo locn:address ?adres }.
            }
          }
        }
      }
    }
  }.
  OPTIONAL {
    ?id m8g:role ?rolId .
    {
   	  SELECT ?rolId ?rolLabel ?rolDefinitie WHERE {
        ?rolId rdf:type skos:Concept .
        ?rolId skos:inscheme dv-conceptscheme:Participatietype .
        ?rolId skos:prefLabel ?rolLabel .
        ?rolId skos:definition ?rolDefinitie .
      }
    }
  }
}
```

## Activeringstraject

**Demo met mocking data**: [Comunica.dev](https://query.comunica.dev/#datasources=https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fswagger%2FR1%2Frelease1.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FTrajectstatustype%2FActief.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FTrajectstatustype%2FPassief.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FTrajectstatustype%2FUitgevoerd.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FTrajectstatustype%2FStopgezet.jsonld&query=PREFIX%20adms%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fadms%23%3E%0APREFIX%20dcterms%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0APREFIX%20m8g%3A%20%3Chttp%3A%2F%2Fdata.europa.eu%2Fm8g%2F%3E%0APREFIX%20schema%3A%20%3Chttps%3A%2F%2Fschema.org%2F%3E%0APREFIX%20kvs1%3A%20%3Chttps%3A%2F%2Fdata.vlaanderen.be%2Fns%2Fklantvolgsysteem1%2F%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20dv-conceptscheme%3A%20%3Chttps%3A%2F%2Fdata.vlaanderen.be%2Fid%2Fconceptscheme%2F%3E%0APREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0A%0A%23%20Each%20variable%20besides%20type%20and%20id%20are%20fully%20optional%20as%20required%20by%20VDAB.%0ASELECT%20%3Fid%20%3Ftype%20%3Fnaam%20%3FstartDatum%20%3FeindDatum%20%3FstatusId%20%3FstatusLabel%20%3FstatusDefinitie%20%3Fparticipant%20%3Fdeeltraject%20WHERE%20%7B%0A%20%20%23%20Get%20all%20Traject%20objects%0A%20%20%3Fid%20rdf%3Atype%20kvs1%3AActiveringstraject.%0A%20%20%3Fid%20rdf%3Atype%20%3Ftype%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20schema%3AstartDate%20%3FstartDatum%20%7D%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20schema%3AendDate%20%3FeindDatum%20%7D%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20m8g%3AhasParticipant%20%3Fparticipant%20%7D%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20dcterms%3AhasPart%20%3Fdeeltraject%20%7D%20.%0A%20%20OPTIONAL%20%7B%20%0A%20%20%20%20%3Fid%20adms%3Astatus%20%3FstatusId%20.%0A%20%20%20%20%7B%0A%20%20%20%20%20%20SELECT%20%3FstatusId%20%3FstatusLabel%20%3FstatusDefinitie%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%3FstatusId%20rdf%3Atype%20skos%3AConcept%20.%0A%20%20%20%20%20%20%20%20%3FstatusId%20skos%3Ainscheme%20dv-conceptscheme%3ATrajectstatustype%20.%0A%20%20%20%20%20%20%20%20%3FstatusId%20skos%3AprefLabel%20%3FstatusLabel%20.%0A%20%20%20%20%20%20%20%20%3FstatusId%20skos%3Adefinition%20%3FstatusDefinitie%20.%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%20.%0A%7D%0A)

**Query**
```
PREFIX adms: <http://www.w3.org/ns/adms#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX m8g: <http://data.europa.eu/m8g/>
PREFIX schema: <https://schema.org/>
PREFIX kvs1: <https://data.vlaanderen.be/ns/klantvolgsysteem1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dv-conceptscheme: <https://data.vlaanderen.be/id/conceptscheme/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

# Each variable besides type and id are fully optional as required by VDAB.
SELECT ?id ?type ?naam ?startDatum ?eindDatum ?statusId ?statusLabel ?statusDefinitie ?participant ?deeltraject WHERE {
  # Get all Traject objects
  ?id rdf:type kvs1:Activeringstraject.
  ?id rdf:type ?type .
  OPTIONAL { ?id schema:startDate ?startDatum } .
  OPTIONAL { ?id schema:endDate ?eindDatum } .
  OPTIONAL { ?id m8g:hasParticipant ?participant } .
  OPTIONAL { ?id dcterms:hasPart ?deeltraject } .
  OPTIONAL {
    ?id adms:status ?statusId .
    {
      SELECT ?statusId ?statusLabel ?statusDefinitie WHERE {
        ?statusId rdf:type skos:Concept .
        ?statusId skos:inscheme dv-conceptscheme:Trajectstatustype .
        ?statusId skos:prefLabel ?statusLabel .
        ?statusId skos:definition ?statusDefinitie .
      }
    }
  } .
}
```

## Deeltraject

**Demo met mocking data**: [Comunica.dev](https://query.comunica.dev/#datasources=https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fswagger%2FR1%2Frelease1.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FTrajectstatustype%2FActief.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FTrajectstatustype%2FPassief.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FTrajectstatustype%2FUitgevoerd.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FTrajectstatustype%2FStopgezet.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FDeeltrajecttype%2FOrientering.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FDeeltrajecttype%2FOpleiding.jsonld;https%3A%2F%2Ftest.data.vlaanderen.be%2Fdoc%2Fimplementatiemodel%2Fklantvolgsysteem1%2Fresources%2Fcodelijsten%2FDeeltrajecttype%2FTender.jsonld&query=PREFIX%20adms%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fadms%23%3E%0APREFIX%20m8g%3A%20%3Chttp%3A%2F%2Fdata.europa.eu%2Fm8g%2F%3E%0APREFIX%20dcterms%3A%20%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0APREFIX%20schema%3A%20%3Chttps%3A%2F%2Fschema.org%2F%3E%0APREFIX%20kvs1%3A%20%3Chttps%3A%2F%2Fdata.vlaanderen.be%2Fns%2Fklantvolgsysteem1%2F%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20dv-conceptscheme%3A%20%3Chttps%3A%2F%2Fdata.vlaanderen.be%2Fid%2Fconceptscheme%2F%3E%0APREFIX%20skos%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0A%0A%23%20Each%20variable%20besides%20type%20and%20id%20are%20fully%20optional%20as%20required%20by%20VDAB.%0ASELECT%20%3Fid%20%3Ftype%20%3Fnaam%20%3FstartDatum%20%3FeindDatum%20%3FstatusId%20%3FstatusLabel%20%3FstatusDefinitie%20%3Fparticipant%20%3FdeeltrajectTypeId%20%3FdeeltrajectTypeLabel%20%3FdeeltrajectTypeDefinitie%20WHERE%20%7B%0A%20%20%23%20Get%20all%20Traject%20objects%0A%20%20%3Fid%20rdf%3Atype%20kvs1%3ADeeltraject.%0A%20%20%3Fid%20rdf%3Atype%20%3Ftype%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20schema%3AstartDate%20%3FstartDatum%20%7D%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20schema%3AendDate%20%3FeindDatum%20%7D%20.%0A%20%20OPTIONAL%20%7B%20%3Fid%20m8g%3AhasParticipant%20%3Fparticipant%20%7D%20.%0A%20%20OPTIONAL%20%7B%20%0A%20%20%20%20%3Fid%20adms%3Astatus%20%3FstatusId%20.%0A%20%20%20%20%7B%0A%20%20%20%20%20%20SELECT%20%3FstatusId%20%3FstatusLabel%20%3FstatusDefinitie%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%3FstatusId%20rdf%3Atype%20skos%3AConcept%20.%0A%20%20%20%20%20%20%20%20%3FstatusId%20skos%3Ainscheme%20dv-conceptscheme%3ATrajectstatustype%20.%0A%20%20%20%20%20%20%20%20%3FstatusId%20skos%3AprefLabel%20%3FstatusLabel%20.%0A%20%20%20%20%20%20%20%20%3FstatusId%20skos%3Adefinition%20%3FstatusDefinitie%20.%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%20.%0A%20%20OPTIONAL%20%7B%20%0A%20%20%20%20%3Fid%20dcterms%3Atype%20%3FdeeltrajectTypeId%20.%0A%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20SELECT%20%3FdeeltrajectTypeId%20%3FdeeltrajectTypeLabel%20%3FdeeltrajectTypeDefinitie%20WHERE%20%7B%0A%20%20%20%20%20%20%20%20%3FdeeltrajectTypeId%20rdf%3Atype%20skos%3AConcept%20.%0A%20%20%20%20%20%20%20%20%3FdeeltrajectTypeId%20skos%3Ainscheme%20dv-conceptscheme%3ADeeltrajecttype%20.%0A%20%20%20%20%20%20%20%20%3FdeeltrajectTypeId%20skos%3AprefLabel%20%3FdeeltrajectTypeLabel%20.%0A%20%20%20%20%20%20%20%20%3FdeeltrajectTypeId%20skos%3Adefinition%20%3FdeeltrajectTypeDefinitie%20.%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%7D%0A%20%20%7D%20.%0A%7D%0A)

**Query**
```
PREFIX adms: <http://www.w3.org/ns/adms#>
PREFIX m8g: <http://data.europa.eu/m8g/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX schema: <https://schema.org/>
PREFIX kvs1: <https://data.vlaanderen.be/ns/klantvolgsysteem1/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dv-conceptscheme: <https://data.vlaanderen.be/id/conceptscheme/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

# Each variable besides type and id are fully optional as required by VDAB.
SELECT ?id ?type ?naam ?startDatum ?eindDatum ?statusId ?statusLabel ?statusDefinitie ?participant ?deeltrajectTypeId ?deeltrajectTypeLabel ?deeltrajectTypeDefinitie WHERE {
  # Get all Traject objects
  ?id rdf:type kvs1:Deeltraject.
  ?id rdf:type ?type .
  OPTIONAL { ?id schema:startDate ?startDatum } .
  OPTIONAL { ?id schema:endDate ?eindDatum } .
  OPTIONAL { ?id m8g:hasParticipant ?participant } .
  OPTIONAL {
    ?id adms:status ?statusId .
    {
      SELECT ?statusId ?statusLabel ?statusDefinitie WHERE {
        ?statusId rdf:type skos:Concept .
        ?statusId skos:inscheme dv-conceptscheme:Trajectstatustype .
        ?statusId skos:prefLabel ?statusLabel .
        ?statusId skos:definition ?statusDefinitie .
      }
    }
  } .
  OPTIONAL {
    ?id dcterms:type ?deeltrajectTypeId .
        {
      SELECT ?deeltrajectTypeId ?deeltrajectTypeLabel ?deeltrajectTypeDefinitie WHERE {
        ?deeltrajectTypeId rdf:type skos:Concept .
        ?deeltrajectTypeId skos:inscheme dv-conceptscheme:Deeltrajecttype .
        ?deeltrajectTypeId skos:prefLabel ?deeltrajectTypeLabel .
        ?deeltrajectTypeId skos:definition ?deeltrajectTypeDefinitie .
      }
    }
  } .
}
```
