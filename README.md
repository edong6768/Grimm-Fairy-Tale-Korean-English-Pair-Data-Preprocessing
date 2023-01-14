# Grimm Fairy Tale Korean-English Pair Data Preprocessing
txt2tsv preprocessing code for Grimm Fairy Tale Data from 'https://m.blog.naver.com/osy2201/222036437318'
- Seperate Korean and English texts and match corresponding pairs
- Remove non story elements (explanatory text, url, title etc.)
- Option to remove dialogue
- Allocate story index (for grouping datapoints from the same story) 
- Save as tsv (tab seperated)

## Processed tsv Data Example
| |story_id|en|ko|
|-|-|-|-|
|0|0|In old times when wishing still helped one, there lived a king whose daughters were all beautiful, but the youngest was so beautiful that the sun itself, which has seen so much, was astonished whenever it shone in her face. Close by the King’s castle ...| 옛날 옛적에 소망을 이루어 주는 힘이 여전히 통했던 때에, 딸들이 모두 예쁜 왕이 한 분 살고 계셨어요. 특히나 막내공주님이 아주 예뻤는데요, 어찌나 아름다운지, 해도 그녀의 얼굴에 햇볕을 비출 때마다 감탄을 하곤 하였더랬죠. 왕의 성은 ...|
|1|0|Now it so happened that on one occasion the princess’s golden ball did not fall into the little hand which she was holding up for it, but on to the ground beyond, and rolled straight into the water. The King’s daughter followed it with her eyes, ...|그러다 우연히 공주의 작은 손으로 떠받치고 있던 황금 공이 바닥으로 떨어져 곧장 우물 속으로 굴러 들어갔지 뭐예요. 공주님이 다급히 눈으론 공을 쫓았지만 ...|
|...|...|...|...|
|2607|210|Therefore, from the most remote times, a green hazel-branch has been the safest protection against adders, snakes, and everything else which creeps on the earth.| 그런 까닭에, 아주 오랜 옛날부터, ‘싱싱하게 푸른’ 개암나무 가지는 독사나 뱀과 같이 땅 위를 기어 다니는 그 밖의 모든 것들로부터 우리를 지켜주는 가장 안전한 보호자가 되어주었답니다.|
