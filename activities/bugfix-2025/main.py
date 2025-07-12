# Copyright (c) yusancky. All rights reserved.
# Licensed under the Apache License 2.0. See License in the project root for license information.

import AllUp_utils.wiki
from collections import defaultdict
from re import findall

RANK_EMOJI = {1: "🥇", 2: "🥈", 3: "🥉"}
RANK_STYLE = {
    1: {"color": "#D6E", "bold": True},
    2: {"color": "#4E4", "bold": True},
    3: {"color": "#4E4", "bold": True},
    4: {"bold": True},
    5: {"bold": True},
}


def show_rank(rank):
    if icon := RANK_EMOJI.get(rank):
        return f"<center>{icon}</center>"
    elif rank <= 5:
        return f'<font style="font-family: TitilliumWeb-Bold";><b>{rank}</b></font>'
    else:
        return f'<font style="font-family: TitilliumWeb-Bold";>{rank}</font>'


def show_score(rank, score):
    st = RANK_STYLE.get(rank, {})
    inner = f"<b>{score}</b>" if st.get("bold") else str(score)
    formatted = (
        f'<font style="font-family: TitilliumWeb-Bold";><center>{inner}</center></font>'
    )
    if color := st.get("color"):
        return f'<font color="{color}">{formatted}</font>'
    return formatted


if __name__ == "__main__":
    leaderboard = '{| class="wikitable" style="background: #FFF"\n! 排名 !! 用户名 !! 总评分\n'
    pattern = r"\{\{天热站破公示\|1\|([^|]+)\|(\d{1,2}\.\d{1,2})\|[^|]+\|[^|]+\|[^|]+\|(\d{1,2})\}\}"
    pulled_content = AllUp_utils.wiki.pull("博客:天热了，让你站破产吧#公示")
    matches = findall(pattern, pulled_content)
    user_scores = defaultdict(int)
    for match in matches:
        username = match[0]
        score = int(match[2])
        user_scores[username] += score
    if sorted_users := sorted(user_scores.items(), key=lambda x: x[1], reverse=True):
        current_rank, same_score_count = 1, 1
        leaderboard += f"|-\n| <center>{show_rank(1)}</center> || <center>[[用户:{sorted_users[0][0]}]]</center> || {show_score(1, sorted_users[0][1])}\n"
        for i in range(1, len(sorted_users)):
            if sorted_users[i][1] == sorted_users[i - 1][1]:
                same_score_count += 1
            else:
                current_rank += same_score_count
                same_score_count = 1
            leaderboard += f"|-\n| <center>{show_rank(current_rank)}</center> || <center>[[用户:{sorted_users[i][0]}]]</center> || {show_score(current_rank, sorted_users[i][1])}\n"
    leaderboard += '|-\n| colspan="3" | 排行榜由<font style="font-family: TitilliumWeb-Bold";>[https://github.com/yusancky/AllUp-Satwiki AllUp]</font>于<small>（北京时间）</small>每天<font style="font-family: TitilliumWeb-Bold";>11</font>时、<font style="font-family: TitilliumWeb-Bold";>15</font>时、<font style="font-family: TitilliumWeb-Bold";>19</font>时、<font style="font-family: TitilliumWeb-Bold";>23</font>时<small>（可能有一定延迟）</small>自动更新。\n|}'
    AllUp_utils.wiki.push("Template:天热站破公示/leaderboard", leaderboard)
