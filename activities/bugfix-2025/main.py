# Copyright (c) yusancky. All rights reserved.
# Licensed under the Apache License 2.0. See License in the project root for license information.

import AllUp_utils.wiki
from collections import defaultdict
from re import findall


def show_rank(rank):
    if icon := {1: "🥇", 2: "🥈", 3: "🥉"}.get(rank):
        return icon
    return f'<font style="font-family: formula1-black";>{rank}</font>'


def show_score(rank, score):
    if rank == 1:
        return f"""<font color="#D6E" style="font-family: formula1-black";><center>{score}</center></font>"""
    if rank <= 3:
        return f"""<font color="#4E4" style="font-family: formula1-black";><center>{score}</center></font>"""
    if rank <= 5:
        return f"""<font style="font-family: formula1-black";><center>{score}</center></font>"""
    if rank <= 7:
        return f"""<font style="font-family: TitilliumWeb-Bold";><center><b>{score}</b></center></font>"""
    return f"""<font style="font-family: TitilliumWeb-Bold";><center>{score}</center></font>"""


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
    leaderboard += '|-\n| colspan="3" | 排行榜由<font style="font-family: formula1-black";>[https://github.com/yusancky/AllUp-Satwiki AllUp]</font>每天<small>（北京时间）</small><font style="font-family: formula1-black";>14</font>时、<font style="font-family: formula1-black";>23</font>时<small>（存在一定延迟）</small>自动更新。\n|}'
    AllUp_utils.wiki.push("Template:天热站破公示/leaderboard", leaderboard)
