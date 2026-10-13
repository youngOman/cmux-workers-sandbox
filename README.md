# cmux-workers-sandbox

cmux-workers 試玩沙盒，可隨時刪除。

執行測試：`python3 -m unittest`

## 命令列用法

```sh
python3 cli.py mean 1 2 3        # 2.0
python3 cli.py median 3 1 2      # 2
python3 cli.py slug "Hello World"  # hello-world
```

參數錯誤（未知子命令、缺參數、非數字、空序列）時，錯誤訊息印到 stderr，exit code 為 2。
