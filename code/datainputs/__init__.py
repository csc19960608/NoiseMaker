# datainputs文件夹中的的代码功能是从sqlite3中读取音乐数据并整理数据格式输入到model中
# melody.py中是读取主旋律数据并整理格式
# chord.py中是读取和弦数据并整理格式
# drum.py是读取鼓点数据并整理格式
# bass.py是读取bass数据并整理格式

# 时间步长：
# 主旋律音符的时间步长是八分之一拍 主旋律组合的时间步长是1拍
# 和弦的时间步长是1拍 和弦生成的时间步长是2拍
# 鼓点音符的时间步长是八分之一拍 鼓点组合的时间步长是2拍
# bass音符的时间步长是八分之一拍 bass组合的时间步长是2拍
# piano_guitar音符的时间步长是四分之一拍 piano_guitar组合的时间步长是2拍
# string音符的时间步长是四分之一拍 string组合的时间步长是2拍
