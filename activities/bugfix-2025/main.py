# Copyright (c) yusancky. All rights reserved.
# Licensed under the Apache License 2.0. See License in the project root for license information.

import AllUp_utils.wiki
from collections import defaultdict
from re import findall

if __name__ == "__main__":
    leaderboard = '{| class="wikitable"\n! 排名 !! 用户名 !! 总评分\n'
    pattern = r"\{\{天热站破公示\|1\|([^|]+)\|(\d{1,2}\.\d{1,2})\|[^|]+\|[^|]+\|[^|]+\|(\d{1,2})\}\}"
    pulled_content = AllUp_utils.wiki.pull("博客:天热了，让你站破产吧")
    matches = findall(pattern, pulled_content)
    user_scores = defaultdict(int)
    for match in matches:
        username = match[0]
        score = int(match[2])
        user_scores[username] += score
    sorted_users = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
    if sorted_users:
        current_rank, same_score_count = 1, 1
        leaderboard += (
            f"|-\n| '''1''' || [[用户:{sorted_users[0][0]}]] || {sorted_users[0][1]}\n"
        )
        for i in range(1, len(sorted_users)):
            if sorted_users[i][1] == sorted_users[i - 1][1]:
                same_score_count += 1
            else:
                current_rank += same_score_count
                same_score_count = 1
            leaderboard += f"|-\n| '''{current_rank}''' || [[用户:{sorted_users[i][0]}]] || {sorted_users[i][1]}\n"
    AllUp_utils.wiki.push("Template:天热站破公示/leaderboard", leaderboard)
