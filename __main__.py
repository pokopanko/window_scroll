import tkinter as tk

# メインウィンドウの作成
root = tk.Tk()
root.title("Resizable Example")
root.geometry("+0+0")  # 左上に固定
root.resizable(False, False)  # サイズ変更不可

# スクロール対応のキャンバス作成
canvas = tk.Canvas(root, width=800, height=600)  # ウィンドウサイズ調整
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

# スクロール可能エリアの設定
scrollable_frame.bind(
    "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# スクロールバーの配置
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


# Expand Main Areaのアクション
def toggle_main_area():
    if var.get():
        main_area.config(width=600, height=400)  # メインエリアを拡張
    else:
        main_area.config(width=300, height=200)  # 元のサイズに戻す


# チェックボックスエリア
var = tk.BooleanVar()
checkbox_area = tk.Frame(scrollable_frame)
checkbox_area.pack(fill="x", pady=5)
checkbox = tk.Checkbutton(
    checkbox_area, text="Expand Main Area", variable=var, command=toggle_main_area
)
checkbox.pack(anchor="w", padx=10)

# メインエリア
main_area = tk.Frame(scrollable_frame, bg="lightblue", width=300, height=200)
main_area.pack(fill="x", pady=5)

file_selection = tk.Label(main_area, text="File Selection Area", bg="lightblue")
file_selection.place(relx=0.5, rely=0.5, anchor="center")

# サブエリア
sub_area = tk.Frame(scrollable_frame, bg="lightgreen", width=600, height=200)
sub_area.pack(fill="x", pady=5)

sub_label = tk.Label(sub_area, text="Sub Area", bg="lightgreen")
sub_label.place(relx=0.5, rely=0.5, anchor="center")

# 実行エリア
exec_area = tk.Frame(scrollable_frame, bg="lightgray", width=600, height=100)
exec_area.pack(fill="x", pady=5)

exec_button = tk.Button(exec_area, text="Execute")
exec_button.place(relx=0.5, rely=0.5, anchor="center")

# ウィンドウのメインループ
root.mainloop()
