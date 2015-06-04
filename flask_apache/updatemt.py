#coding:utf-8
__author__ = 'JYC103'

import subprocess,shutil,time,os



class UpdateMtVersion():
    dir_mt_server_192 = r'G:\update_mt_tmp\192_url\all_mt_server'
    dir_mt_resource_192 = r'G:\update_mt_tmp\192_url\all_mt_resource'

    dir_mt_183 = r'F:\mtservion\mt_all'
    dir_mt_server_183 = r'F:\mtservion\mt_all\all_mt_server'
    dir_mt_resource_183 = r'F:\mtservion\mt_all\all_mt_resource'

    svn_url_mt_server_192 = r'svn://192.168.10.202/mt_rel/server/ttaxy/release'
    svn_url_mt_resource_192 = r'svn://192.168.10.202/mt_rel/resource/ttaxy/release'

    nowtiem = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    outlog = 'out.'+ nowtiem + '.log'
    outfile = open(r'out.log',"a+")



    def update_mt_183(self):
        update_cmd = subprocess.Popen('svn cleanup && svn update %s' %self.dir_mt_183,
                                      shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdoutdata,stderrdata=update_cmd.communicate()
        if stderrdata is not None and stdoutdata is not None:
            stdoutdata = ''.join(stderrdata)
            return self.outfile.write(stdoutdata)
            #print stdoutdata
        elif stdoutdata is None and stderrdata is not None:
            return self.outfile.write(stdoutdata)
            #print stderrdata
        elif stderrdata is None and stdoutdata is not None:
            return self.outfile.write(stdoutdata)
            #print stdoutdata
        else:
            exit(0)


    def export_mt_192(self,version_mt_192,svn_url_mt_192,dir_mt_192):
        if os.path.exists(dir_mt_192):
            shutil.rmtree(dir_mt_192)
        export_cmd = subprocess.Popen('svn export -r %s %s %s' %(version_mt_192,svn_url_mt_192,dir_mt_192),
                                      shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdoutdata,stderrdata=export_cmd.communicate()
        if stderrdata is not None and stdoutdata is not None:
            stdoutdata = ''.join(stderrdata)
            return self.outfile.write(stdoutdata)
            #print stdoutdata
        elif stdoutdata is None and stderrdata is not None:
            #print stderrdata
            return self.outfile.write(stdoutdata)
        elif stderrdata is None and stdoutdata is not None:
            #print stdoutdata
            return self.outfile.write(stdoutdata)
        else:
            exit(0)

    def cp_add_ci_mt_183(self,dir_mt_192,dir_mt_183):
        i_cmd = ['xcopy /S /Y %s %s' %(dir_mt_192,dir_mt_183),'svn add %s/*' %dir_mt_183,'svn ci -m "update mt_server" %s' %dir_mt_183]
        for j_cmd in i_cmd:
            cp_add_ci_mt_cmd = subprocess.Popen(j_cmd,shell=True,universal_newlines=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            stdoutdata,stderrdata=cp_add_ci_mt_cmd.communicate()
            if stderrdata is not None and stdoutdata is not None:
                stdoutdata = ''.join(stderrdata)
                return self.outfile.write(stdoutdata)
                #print stdoutdata
            elif stdoutdata is None and stderrdata is not None:
                #print stderrdata
                return self.outfile.write(stdoutdata)
            elif stderrdata is None and stdoutdata is not None:
                #print stdoutdata
                return self.outfile.write(stdoutdata)
            else:
                exit(0)


    def main(self,mt_server_version,mt_resource_version):
        #self.createlog()
        self.update_mt_183()
        if mt_resource_version == 1:
            self.export_mt_192(mt_server_version,self.svn_url_mt_server_192,self.dir_mt_server_192)
            self.cp_add_ci_mt_183(self.dir_mt_server_192,self.dir_mt_server_183)
        elif mt_server_version ==1:
            self.export_mt_192(mt_resource_version,self.svn_url_mt_resource_192,self.dir_mt_resource_192)
            self.cp_add_ci_mt_183(self.dir_mt_resource_192,self.dir_mt_resource_183)
        elif mt_resource_version ==1 and mt_server_version ==1:
            #print 'exit now'
            exit(0)
        else:
            exit(0)




