#coding:utf-8
__author__ = 'JYC103'

import paramiko,time

mt_local_dir=r'/data/mix_mtserver_local'
mt_online_dir=r'/data/mix_mtserver_online'
local_ip='192.168.164.225'
username="root"
port=22
password="qwe34%^QWE"
pkey_w='1254'
try:
    pkey=paramiko.RSAKey.from_private_key_file(pkey_w)
except paramiko.PasswordRequiredException:
    pkey=paramiko.RSAKey.from_private_key_file(pkey_w,password)


def ssh_con(ip,username,pkey,cmd):
    ssh=paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip,username=username,port=22,pkey=pkey)
    for m in cmd:
        stdin,stdout,stderr=ssh.exec_command(m)
        out=stdout.readlines()
        for o in out:
            if not o:
                print "error %s" %ip
                break
            else:
                print o.strip()
    ssh.close()


def update_server(version_num):
    clean_server_local_dir_cmd=['rm -rf %s/mt_server' %(mt_local_dir)]
    export_server_local_cmd=['svn export -r %s svn://192.168.10.202/mt_rel/server/ttaxy/release %s/mt_server' %(version_num,mt_local_dir)]
    cp_server_cmd=['svn up %s/mt_server' %(mt_online_dir),'cp -rfv %s/mt_server %s' %(mt_local_dir,mt_online_dir)]
    commite_online_mt_cmd=['svn add %s/mt_server/*' %mt_online_dir,'svn ci -m "update mt_server to version %s" %s/mt_server/' %(version_num,mt_online_dir)]
    server_update_cmd=['/usr/mtinit/mtServer all stop','svn up /usr/mtserver/mt_server','/usr/mtinit/upserver_svn_new all','/usr/mtinit/mtServer all start']
    print 'update Development mt_server version to location %s '  %local_ip
    '''
    try:
        ssh_con(local_ip,username,pkey,clean_server_local_dir_cmd)
        print 'the mt_server dir clean completed'
    except:
        print 'the mt_server no exist'
    ssh_con(local_ip,username,pkey,export_server_local_cmd)
    ssh_con(local_ip,username,pkey,cp_server_cmd)
    '''
    return ssh_con(local_ip,username,pkey,clean_server_local_dir_cmd),ssh_con(local_ip,username,pkey,export_server_local_cmd),ssh_con(local_ip,username,pkey,cp_server_cmd)

    '''
    ssh_con(local_ip,username,pkey,commite_online_mt_cmd)

    file=open("F:/abc/server_ip.txt")
    f=file.readlines()
    for ip in f:
        print ip.strip()
        ssh_con(ip.strip(),username,pkey,server_update_cmd)
    file.close()
    '''


def update_resource(version_num):
    clean_resource_local_dir_cmd=['rm -rf %s/mt_resource' %(mt_local_dir)]
    export_resource_local_cmd=['svn export -r %s svn://192.168.10.202/mt_rel/resource/ttaxy/release %s/mt_resource' %(version_num,mt_local_dir)]
    cp_resource_cmd=['svn up %s/mt_resource' %(mt_online_dir),'cp -rfv %s/mt_resource %s' %(mt_local_dir,mt_online_dir)]
    commite_online_mt_cmd=['svn add %s/mt_resource/*' %mt_online_dir,'svn ci -m "update mt_resource to version %s" %s/mt_resource/' %(version_num,mt_online_dir)]
    resource_update_cmd=['svn up /usr/mtserver/mt_resource','/usr/mtinit/upresource_svn_new all']
    print 'update Development mt_resource version to location %s '  %local_ip
    '''
    try:
        ssh_con(local_ip,username,pkey,clean_resource_local_dir_cmd)
        print 'the mt_resource dir clean completed'
    except:
        print 'the mt_resource no exist'
    ssh_con(local_ip,username,pkey,export_resource_local_cmd)
    ssh_con(local_ip,username,pkey,cp_resource_cmd)
    '''
    return ssh_con(local_ip,username,pkey,clean_resource_local_dir_cmd),ssh_con(local_ip,username,pkey,export_resource_local_cmd),ssh_con(local_ip,username,pkey,cp_resource_cmd)

    '''
    ssh_con(local_ip,username,pkey,commite_online_mt_cmd)

    file=open("F:/abc/server_ip.txt")
    f=file.readlines()
    for ip in f:
        print ip.strip()
        ssh_con(ip.strip(),username,pkey,resource_update_cmd)
    file.close()
    '''

'''
#def mt_server_svn_up():
if __name__=='__main__':
    print 'update mt_server or mt_resource or update all'
    mt_input=raw_input('please input (mt_server mt_resource all) one choice:')
    if mt_input == 'mt_server':
        version_num=int(raw_input('input mt_server Development version num:'))
        print 'Development mt_server version %s' %version_num
        update_server(version_num)
    elif mt_input == 'mt_resource':
        version_num=int(raw_input('input mt_resource Development version num:'))
        print 'Development mt_resource version %s' %version_num
        update_resource(version_num)
    elif mt_input == 'all':
        version_num_resource=int(raw_input('input mt_resource Development version num:'))
        print 'Development mt_resource version %s' %version_num_resource
        version_num_server=int(raw_input('input mt_server Development version num:'))
        print 'Development mt_server version %s' %version_num_server
        update_resource(version_num_resource)
        update_server(version_num_server)
        '''










