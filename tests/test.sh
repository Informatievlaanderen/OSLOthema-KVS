#!/bin/sh
set -e

# JSON-LD context
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/doc/implementatiemodel/klantvolgsysteem1/ontwerpstandaard/2025-11-04/context/KVS-R1.jsonld

# SHACL shapes
curl --fail-with-body -L -H 'Accept: text/turtle' https://data.vlaanderen.be/doc/implementatiemodel/klantvolgsysteem1/ontwerpstandaard/2025-11-04/shacl/KVS-R1-SHACL.ttl

# Conceptschemes
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/conceptscheme/Deeltrajecttype
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/conceptscheme/OrganisatieType
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/conceptscheme/PubliekeDienstverleningType
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/conceptscheme/Voorkeurtype
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/conceptscheme/FinaliteitType
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/conceptscheme/Participatietype
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/conceptscheme/Trajectstatustype

# Concepts
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Deeltrajecttype/Opleiding
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Deeltrajecttype/Orientering
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Deeltrajecttype/Tender
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/OrganisatieType/VDAB
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/OrganisatieType/OCMW
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/PubliekeDienstverleningType/ActiveringNaarWerk
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Voorkeurtype/GewenstBeroep
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Voorkeurtype/TeLerenBeroep
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Voorkeurtype/TeVerkennenBeroep
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Voorkeurtype/UitgeslotenBeroep
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/FinaliteitType/SociaalOnderzoek
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/FinaliteitType/GPMI
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Participatietype/Begeleider
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Participatietype/Bemiddelaar
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Participatietype/Contactpersoon
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Participatietype/Werkzoekende
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Trajectstatustype/Actief
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Trajectstatustype/Passief
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Trajectstatustype/Stopgezet
curl --fail-with-body -L -H 'Accept: application/ld+json' https://data.vlaanderen.be/id/concept/Trajectstatustype/Uitgevoerd
