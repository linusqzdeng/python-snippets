import subpackage1.n1

print('name: ' + __name__) # 被当作应用程序的入口(入口文件)时返回'__main__'
print('package: ' + (__package__ or 'This module does not belong to any packages'))
print('doc: ' + (__doc__ or 'This module does not have an interpretation'))
print('file: ' + __file__)
