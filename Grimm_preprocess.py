import re
import pandas as pd
from tqdm import tqdm


def en_ko_split(paragraph:str, rv_dlg=False):
    
    # remove dialog
    if rv_dlg:
        dialog_match = "(“[^‘“”]*”|‘[^‘“”]*’)"
        paragraph = re.sub(dialog_match, '', paragraph)
        
    # split Eng and Kor sentences 
    ko_match = "\n*[“‘]?\d*[가-힣]+[\d.,;“”’?!\s\n…]*[”’]?\n*"
    
    en = re.sub(ko_match, '', paragraph)
    ko = ''.join(re.findall(ko_match, paragraph))
    
    if not (en and ko and re.match('[A-Za-z]', en)): return None
    
    en = en.replace('\n', ' ')
    ko = ko.replace('\n', ' ')
    
    return en, ko
    

def text_test():
    text = """After a year or so had passed, the Queen brought a son into the world. Thereupon the Virgin Mary appeared to her in the night when she lay in her bed alone, and said, “If thou wilt tell the truth and confess that thou didst unlock the forbidden door, I will open thy mouth and give thee back thy speech, but if thou perseverest in thy sin, and deniest obstinately, I will take thy new-born child away with me.”
1년 쯤 지나고, 왕비가 아들을 낳았어요.
그 후 즉시, 왕비가 밤에 홀로 침대에 누워있을 때, 성모 마리아께서 오셔서 말씀하셨어요.
“만약 네가 진실을 말하고 금지된 방문을 열어봤다 내게 아뢴다면, 너의 입을 열어주고 목소리도 돌아오게 할 것이데, 하지만 네 잘못을 인정치 않고 완강히 거짓을 말한다면, 내 네 아이를 데리고 갈 것이다.” ”"""
    print(en_ko_split(text))
    quit()


if __name__=='__main__':
    f_root = "./"

    # open file
    f_path = f_root + "fairy_tale_grimm_original.txt"
    with open(f_path, "r", encoding="utf-8") as f :
        text = f.read()

    # delete unnecesary sentences between different stories and split
    story_end = "\(끝\)" + "\n+.+"*5 + "\n+"
    stories = re.split(story_end, text)

    # split a story into paragraphs and split english and korean
    parag_pairs = []
    for n, story in enumerate(tqdm(stories)):
        story = re.sub("(\(?https?://.*\)?|\([^\(\)]+\))", "", story)
        
        for parag in re.split("\n{2,}", story):
            en_ko = en_ko_split(parag)
            if not en_ko: continue
            parag_pairs.append((n, *en_ko))
        
    # save
    df = pd.DataFrame(parag_pairs, columns=('story_id', 'en', 'ko'))
    df.to_csv(f_root+"fairy_tale_grimm.tsv", mode='w', encoding='utf-8', sep="\t")
