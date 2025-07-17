from src.database.redis.taskq import send_cre, send_opt

send_cre.delay("anasothman581@gmail.com", "ClientName", "some-verification-token")
send_opt.delay()
