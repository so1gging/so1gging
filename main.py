import feedparser
import time
URL="https://yzlosmik.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
# Hi, THERE 👋🏻
> 유연한 코드를 늘 고민하는 **프론트 엔지니어** 입니다. 🌱

<a href="https://github.com/devxb/gitanimals">
<img
  src="https://render.gitanimals.org/farms/so1gging"
  width="600"
  height="300"
/>
</a>

#### 📚 제 Tech stack은 아래와 같아요.
<div align="left">
	<img src="https://img.shields.io/badge/React-61DAFB?style=flat&logo=React&logoColor=white" />
  <img src="https://img.shields.io/badge/typescript-3178C6?style=flat&logo=typescript&logoColor=white" />
	<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=HTML5&logoColor=white" />
	<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=CSS3&logoColor=white" />
	<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=JavaScript&logoColor=white" />
  <br/>
  	<img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white" />
    	<img src="https://img.shields.io/badge/webstorm-000000?style=flat&logo=webstorm&logoColor=white" />
</div>
<br>

#### ✨ New posts
"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']})\n"
markdown_text +=  """
</div>
</div>
"""
print(markdown_text)
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
