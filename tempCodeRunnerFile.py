    for row in range(3):
            if i == 1:
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = i*0.4
                elif enemyX[i] >= 736:
                    enemyX_change[i] = i*-0.4
            if i == 2:
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 200:
                    enemyX_change[i] = i*0.4
                elif enemyX[i] >= 600:
                    enemyX_change[i] = i*-0.4
            if i == 3:
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 300:
                    enemyX_change[i] = i*0.4
                elif enemyX[i] >= 500:
                    enemyX_change[i] = i*-0.4
