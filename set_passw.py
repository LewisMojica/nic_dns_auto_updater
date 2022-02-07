import keyring

usern, passw = 'my username','a very strong password'

keyring.set_password('nic_dns_auto_updater', usern, passw)

