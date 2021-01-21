from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType


words = [
    ("张栋杰", 1.0),
    ("張棟傑", 0.8),
    ("ちょうとうけつ", 0.5),
    ("顾琳", 0.9),
    ("ZhangMochi", 1.0),
    ("张墨弛", 1.0),
    ("爷爷", 0.8),
    ("奶奶", 0.8),
    ("外婆", 0.8),
    ("外公", 0.8)
]


def wordcloud() -> WordCloud:
    c = (
        WordCloud()
        # word_size_range: 单词字体大小范围
        .add("", words, word_size_range=[10, 100], shape='cardioid')
        .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud"))
    )
    return c


wordcloud().render('./img/wordcloud.html')