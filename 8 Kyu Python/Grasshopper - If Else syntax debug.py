def check_alive(health):
    if health >= -10 and health <= 10:
        if health <= 0:
            return False
        else: 
            return True
