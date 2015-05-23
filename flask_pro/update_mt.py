#coding:gbk
__author__ = 'JYC103'

import os,shutil,sys
sys.getdefaultencoding()

class UpdateMtVersion():
    dir_mt_server_192 = r'G:\update_mt_tmp\192_url\all_mt_server'
    dir_mt_resource_192 = r'G:\update_mt_tmp\192_url\all_mt_resource'

    dir_mt_183 = r'F:\mtservion\mt_all'
    dir_mt_server_183 = r'F:\mtservion\mt_all\all_mt_server'
    dir_mt_resource_183 = r'F:\mtservion\mt_all\all_mt_resource'

    svn_url_mt_server_192 = r'svn://192.168.10.202/mt_rel/server/ttaxy/release'
    svn_url_mt_resource_192 = r'svn://192.168.10.202/mt_rel/resource/ttaxy/release'



    def export_mt_192(self,version_mt_192,svn_url_mt_192,dir_mt_192):
        if os.path.exists(dir_mt_192):
            shutil.rmtree(dir_mt_192)
        os.system('svn export -r %s %s %s' %(version_mt_192,svn_url_mt_192,dir_mt_192))

    def update_mt_183(self):
        os.system('svn update %s' %self.dir_mt_183)

    def cp_add_ci_mt_183(self,dir_mt_192,dir_mt_183):
        os.system('xcopy /S /Y %s %s' %(dir_mt_192,dir_mt_183))
        os.system('svn add %s/*' %dir_mt_183)
        os.system('svn ci -m "update mt_server" %s' %dir_mt_183)

    def main(self,mt_server_version,mt_resource_version):
        if int(mt_resource_version) == 0:
            self.export_mt_192(mt_server_version,self.svn_url_mt_server_192,self.dir_mt_server_192)
#           cp_add_ci_mt_183(dir_mt_server_192,dir_mt_server_183)






# if __name__=='__main__':
#     abc=UpdateMtVersion()
#     print abc.dir_mt_resource_183



# if __name__=='__main__':
#     update_mt_183()
#     update_select = raw_input('只更新服务端输入:mt_server；只更新配置表输入:mt_resource；更新全部内容输入:all；  :')
#     if update_select == 'mt_server':
#         version_mt_server_192 = int(raw_input('input version_mt_server_192:'))
#         export_mt_192(version_mt_server_192,svn_url_mt_server_192,dir_mt_server_192)
#         cp_add_ci_mt_183(dir_mt_server_192,dir_mt_server_183)
#     elif update_select == 'mt_resource':
#         version_mt_resource_192 = int(raw_input('input version_mt_resource_192:'))
#         export_mt_192(version_mt_resource_192,svn_url_mt_resource_192,dir_mt_resource_192)
#         cp_add_ci_mt_183(dir_mt_resource_192,dir_mt_resource_183)
#     elif update_select == 'all':
#         version_mt_server_192 = int(raw_input('input version_mt_server_192:'))
#         version_mt_resource_192 = int(raw_input('input version_mt_resource_192:'))
#         export_mt_192(version_mt_server_192,svn_url_mt_server_192,dir_mt_server_192)
#         export_mt_192(version_mt_resource_192,svn_url_mt_resource_192,dir_mt_resource_192)
#         cp_add_ci_mt_183(dir_mt_server_192,dir_mt_server_183)
#         cp_add_ci_mt_183(dir_mt_resource_192,dir_mt_resource_183)
#     else:
#         print 'error input,exit now.'
#         exit(0)









