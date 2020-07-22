# auther:shixingjian  time:2020/6/25/0025
#1.向网页发出请求
import requests
import re
import socket
#存储初始化-----------
import xlwt
#创建Excel
workBook = xlwt.Workbook(encoding='utf-8')
#在文件对象创建一个sheet
workSheet = workBook.add_sheet('51job.res')
#创建列名
colName = ['职位名','公司名','公司地点','薪资','发布时间']
for col in range(0,len(colName)):#(行，列，内容）
    workSheet.write(0,col,colName[col])
def get_webPage():
    user_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    web_url = 'https://search.51job.com/list/140600%252C020000,000000,2707,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    resp = requests.get(web_url,headers = user_header)
    resp.encoding = 'gbk'
    pages = re.findall('<span class="td">共(.*?)页，到第</span>',resp.text,re.S)
    return int(pages[0])
#----------获取所有页-----------------
line = 1
for page in range(1,get_webPage()+1):
    socket.setdefaulttimeout(20)
    user_header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    web_url = f'https://search.51job.com/list/140600%252C020000,000000,2707,00,9,99,%2520,2,{page}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    res = requests.get(web_url,headers = user_header)

    #保存
    # workBook.save('f:\\51job.xls')
    #2.解析网页数据
    res.encoding = 'gbk'
    #print(res.text)
    #3.提取需要的数据
    info = re.findall('<div class="el">(.*?)</div>',res.text,re.S)
    #print(info[0])
    for one in info:
        temp = re.findall('a target="_blank" title="(.*?)" href=',one,re.S)
        #岗位名称：
        jobName = temp[0]
        workSheet.write(line,0,jobName)
        # 公司名称：
        companyName = temp[1]
        workSheet.write(line, 1, companyName)
        # 地点名称：
        address = re.findall('<span class="t3">(.*?)</span>', one, re.S)[0]
        workSheet.write(line, 2, address)
        # 薪资：
        salary = re.findall('<span class="t4">(.*?)</span>', one, re.S)[0]
        workSheet.write(line, 3, salary)
        # 日期名称：
        time = re.findall('<span class="t5">(.*?)</span>', one, re.S)[0]
        workSheet.write(line, 4, time)
        #print(jobName,companyName,address,salary,time)
        line += 1
#4.存储数据---excel
workBook.save('f:\\51job.xls')


'''
<div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="47840680" jt="0" style="display:none">
            <span>
                <a target="_blank" title="农药残留测试工程师" href="https://jobs.51job.com/shanghai-xhq/47840680.html?s=01&amp;t=0" onmousedown="">
                    农药残留测试工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="SGS通标标准技术服务有限公司上海分公司" href="https://jobs.51job.com/all/co639755.html">SGS通标标准技术服务有限公司上海...</a></span>
        <span class="t3">上海-徐汇区</span>
        <span class="t4">6-8千/月</span>
        <span class="t5">06-25</span>
    </div>

'''