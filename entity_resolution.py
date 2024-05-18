import pandas as pd

class EntityResolution:

    """
    This class compares the matches from FERN with VEEr
    """

    def __init__(self, encoder, client, entity_df):
        self.client = client
        self.encoder = encoder
        self.entity_df = entity_df


    def compare_matches(self, entity_id):
        hits = self.client.search(
            collection_name="entities",
            query_vector= self.encoder.encode(
                self.entity_df[self.entity_df['ID'] == entity_id]['entity'].values[0]
            ).tolist(),
            limit=10
        )
        attributes = []
        entity_ids = []
        score = []
        veer_df = pd.DataFrame()
        for hit in hits:
                if hit.score > 0.7:
                    if hit.payload['entity_id'] != entity_id:
                        attributes.append(hit.payload['attributes'])
                        entity_ids.append(hit.payload['entity_id'])
                        score.append(round(hit.score, 6))
        veer_df['entity_id'] = entity_ids
        veer_df['combined_attribute'] = attributes
        veer_df['score'] = score
        return veer_df