def generate_psc_dump(admin_passwd):
    get_cmd = "ldapsearch -b \"dc=vmc,dc=local\" -s sub -D \"cn=Administrator,cn=Users,dc=vmc,dc=local\" -W"
    child = pexpect.spawn(get_cmd)
    fd = open("/tmp/PSC_FQDN.ldif", "wb")
    child.logfile_read = fd
    child.expect("Enter LDAP Password:")
    child.sendline(admin_passwd)
    child.expect(pexpect.EOF)
    print("PSC config Dump file location: {}".format(fd.name))
    fd.close()
    return 0
