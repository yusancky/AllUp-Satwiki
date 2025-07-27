# Copyright (c) yusancky. All rights reserved.
# Licensed under the Apache License 2.0. See License in the project root for license information.

import AllUp_utils.wiki
from collections import defaultdict
from re import findall


def show_rank(rank):
    if icon := {1: "🥇", 2: "🥈", 3: "🥉"}.get(rank):
        return icon
    return str(rank)


def show_score(rank, score):
    if rank == 1:
        return f"""<font color="#D6E">{score}</font>"""
    if rank <= 3:
        return f"""<font color="#4E4">{score}</font>"""
    if score >= 100:
        return str(score)
    return f"""<font style="font-family: TitilliumWeb-Bold";>{score}</font>"""


if __name__ == "__main__":
    leaderboard = '{| class="wikitable" style="background: #FFF;text-align:center;"\n! 排名 !! 用户名 !! 总评分\n'
    pattern = r"\{\{天热站破公示\|1\|([^|]+)\|(\d{1,2}\.\d{1,2})\|[^|]+\|[^|]+\|[^|]+\|(\d{1,2})\}\}"
    pulled_content, revid = AllUp_utils.wiki.pull(
        "博客:天热了，让你站破产吧#公示"
    ), AllUp_utils.wiki.get_last_revid("博客:天热了，让你站破产吧")
    matches = findall(pattern, pulled_content)
    user_scores = defaultdict(int)
    for match in matches:
        username = match[0]
        score = int(match[2])
        user_scores[username] += score
    if sorted_users := sorted(user_scores.items(), key=lambda x: x[1], reverse=True):
        current_rank, same_score_count = 1, 1
        leaderboard += f"|-\n| {show_rank(1)} || [[用户:{sorted_users[0][0]}]] || {show_score(1, sorted_users[0][1])}\n"
        for i in range(1, len(sorted_users)):
            if sorted_users[i][1] == sorted_users[i - 1][1]:
                same_score_count += 1
            else:
                current_rank += same_score_count
                same_score_count = 1
            leaderboard += f"|-\n| {show_rank(current_rank)} || [[用户:{sorted_users[i][0]}]] || {show_score(current_rank, sorted_users[i][1])}\n"
    leaderboard += f'|-\n| colspan="3" style="text-align:left;" | 排行榜由[https://github.com/yusancky/AllUp-Satwiki AllUp]每小时自动获取数据并更新。<small>上次更新：<code>[https://sat.huijiwiki.com/w/index.php?title=博客:天热了，让你站破产吧&oldid={revid} @{revid}]</code></small>\n|}}'
    AllUp_utils.wiki.push("Template:天热站破公示/leaderboard", leaderboard)
