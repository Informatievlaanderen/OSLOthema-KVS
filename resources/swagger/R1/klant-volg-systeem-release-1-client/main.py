from klant_volg_systeem_release_1_client import Client
from klant_volg_systeem_release_1_client.api.dienstverlening import get_service
from klant_volg_systeem_release_1_client.models import (
    ActiveringstrajectType,
    JsonLdRoot,
    WerkvoorkeurenType,
)
from klant_volg_systeem_release_1_client.types import Response

TITEL_NAAM_BEROEP = "Beroep Label"
TITEL_TAAL_BEROEP = "Taal Beroep Label"
TITEL_VOORKEUR_ID = "Voorkeur ID"

# @id zou eigenlijk best een label zijn die geresolved is in de context, dan krijg je nette types in Swagger

if __name__ == "__main__":
    client = Client(base_url="http://localhost:8000/")
    root: JsonLdRoot = get_service.sync(client=client, x_insz="123456789", x_correlation_id="wsalsfdhjdslfjds")
    response: Response[JsonLdRoot] = get_service.sync_detailed(
        client=client, x_insz="123456789", x_correlation_id="wsalsfdhjdslfjds"
    )
    for obj in root.graph:
        print(obj.type_)
        if obj.type_ == WerkvoorkeurenType.WERKVOORKEUREN:
            print(f"| {TITEL_NAAM_BEROEP:>20} | {TITEL_TAAL_BEROEP:>20} | {TITEL_VOORKEUR_ID:>70} |")
            print("|" + "-" * 118 + "|")
            for beroepstoestand in obj.werkvoorkeuren_beroep:
                print(
                    f"| {beroepstoestand.beroepstoestand_naam.value:>20} | {beroepstoestand.beroepstoestand_naam.language:>20} | {beroepstoestand.beroepstoestand_voorkeur.id:>70} |"
                )

        if obj.type_ == ActiveringstrajectType.ACTIVERINGSTRAJECT:
            for deeltraject in obj.activeringstraject_deeltraject:
                print(deeltraject.deeltraject_type)

    print(response)
    print(response.links)
