# index.html グラスモーフィズム リデザイン 実装プラン

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `index.html` のCSSをグラスモーフィズム×オーロラカラーに刷新し、視認性を保ちながらおしゃれなデザインにする。

**Architecture:** `index.html` 内の `<style>` タグのみ変更。HTMLタグ・クラス名・JavaScript一切変更なし。ブラウザで開いて目視確認する。

**Tech Stack:** HTML/CSS（pure）、`backdrop-filter`（モダンブラウザ対応）

---

### Task 1: ブランチ作成

**Files:**
- 変更なし（git操作のみ）

- [ ] **Step 1: フィーチャーブランチを作成する**

```bash
cd "/Users/tomitamasaki/ai-management:/my-first-repo"
git checkout -b feature/glassmorphism-redesign
```

Expected: `Switched to a new branch 'feature/glassmorphism-redesign'`

---

### Task 2: body・コンテナのCSSを置き換える

**Files:**
- Modify: `index.html`（`<style>` タグ内 `body` と `.container` セレクタ）

- [ ] **Step 1: `body` のスタイルを変更する**

`index.html` の `body { ... }` を以下に置き換える：

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #a18cd1 0%, #fbc2eb 50%, #a6c1ee 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}
```

- [ ] **Step 2: `.container` のスタイルを変更する**

`.container { ... }` を以下に置き換える：

```css
.container {
    background: rgba(255, 255, 255, 0.72);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255, 255, 255, 0.85);
    border-radius: 24px;
    box-shadow: 0 8px 40px rgba(160, 130, 210, 0.3);
    max-width: 500px;
    width: 100%;
    padding: 40px;
}
```

- [ ] **Step 3: ブラウザで確認する**

```bash
open "/Users/tomitamasaki/ai-management:/my-first-repo/index.html"
```

Expected: オーロラグラデーション背景に半透明白カードが表示される。

---

### Task 3: タイトル・テキスト色を変更する

**Files:**
- Modify: `index.html`（`h1`、`.empty-message`、`.stats` セレクタ）

- [ ] **Step 1: `h1` の色を変更する**

`h1 { ... }` を以下に置き換える：

```css
h1 {
    color: #2d1b4e;
    text-align: center;
    margin-bottom: 30px;
    font-size: 28px;
}
```

- [ ] **Step 2: `.empty-message` と `.stats` の色を変更する**

```css
.empty-message {
    text-align: center;
    color: #9b7fc0;
    padding: 40px 20px;
    font-size: 16px;
}

.stats {
    text-align: center;
    margin-top: 20px;
    padding-top: 20px;
    border-top: 1px solid rgba(161, 140, 209, 0.3);
    color: #9b7fc0;
    font-size: 14px;
}
```

- [ ] **Step 3: ブラウザで確認する**

タイトル「To Do リスト」がダークパープル（`#2d1b4e`）で表示されること。白背景に埋もれず読みやすいこと。

---

### Task 4: 入力欄・追加ボタンのスタイルを変更する

**Files:**
- Modify: `index.html`（`#taskInput`、`#addBtn`、`#addBtn:hover`、`#addBtn:active` セレクタ）

- [ ] **Step 1: `#taskInput` のスタイルを変更する**

```css
#taskInput {
    flex: 1;
    padding: 12px 16px;
    border: 1.5px solid rgba(161, 140, 209, 0.4);
    border-radius: 12px;
    font-size: 16px;
    background: rgba(255, 255, 255, 0.6);
    color: #3d2260;
    outline: none;
    transition: border-color 0.3s;
}

#taskInput::placeholder {
    color: #b49fd4;
}

#taskInput:focus {
    border-color: #c084fc;
}
```

- [ ] **Step 2: `#addBtn` のスタイルを変更する**

```css
#addBtn {
    padding: 12px 24px;
    background: linear-gradient(135deg, #a18cd1 0%, #c084fc 100%);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
}

#addBtn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 16px rgba(161, 140, 209, 0.5);
}

#addBtn:active {
    transform: translateY(0);
}
```

- [ ] **Step 3: ブラウザで確認する**

入力欄が半透明白、追加ボタンが紫グラデーションで表示されること。

---

### Task 5: タスク項目のスタイルを変更する

**Files:**
- Modify: `index.html`（`.task-item`、`.task-item:hover`、`.task-item.completed`、`.task-item.completed .task-text`、`.checkbox`、`.task-text`、`.delete-btn`、`.delete-btn:hover` セレクタ）

- [ ] **Step 1: `.task-item` のスタイルを変更する**

```css
.task-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 16px;
    background: rgba(255, 255, 255, 0.55);
    border: 1px solid rgba(161, 140, 209, 0.25);
    border-radius: 14px;
    margin-bottom: 8px;
    transition: all 0.3s;
}

.task-item:hover {
    background: rgba(255, 255, 255, 0.7);
}

.task-item.completed {
    opacity: 0.6;
}

.task-item.completed .task-text {
    text-decoration: line-through;
    color: #9b7fc0;
}
```

- [ ] **Step 2: `.checkbox`、`.task-text`、`.delete-btn` のスタイルを変更する**

```css
.checkbox {
    width: 20px;
    height: 20px;
    cursor: pointer;
    accent-color: #c084fc;
    flex-shrink: 0;
}

.task-text {
    flex: 1;
    color: #2d1b4e;
    font-size: 16px;
    font-weight: 500;
    word-break: break-word;
}

.delete-btn {
    background: rgba(251, 194, 235, 0.4);
    color: #a0538a;
    border: 1px solid rgba(251, 194, 235, 0.7);
    border-radius: 8px;
    padding: 6px 12px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 600;
    transition: background 0.2s;
    flex-shrink: 0;
}

.delete-btn:hover {
    background: rgba(251, 194, 235, 0.7);
}
```

- [ ] **Step 3: ブラウザで確認する**

- タスクテキストが `#2d1b4e` で読みやすく表示されること
- 完了タスクが打ち消し線＋`#9b7fc0` 色で表示されること
- 削除ボタンがピンク系で表示されること

---

### Task 6: 最終確認とコミット

**Files:**
- 変更なし（確認・git操作のみ）

- [ ] **Step 1: ブラウザで全機能を動作確認する**

```bash
open "/Users/tomitamasaki/ai-management:/my-first-repo/index.html"
```

確認項目：
- タスク追加が動作すること
- チェックボックスで完了切り替えができること
- 削除ボタンが動作すること
- ページリロード後もタスクが残ること（localStorage確認）
- 全テキストが読みやすいこと

- [ ] **Step 2: コミットする**

```bash
cd "/Users/tomitamasaki/ai-management:/my-first-repo"
git add index.html
git commit -m "Redesign index.html with glassmorphism aurora style"
```

- [ ] **Step 3: GitHubにプッシュする**

```bash
git push -u origin feature/glassmorphism-redesign
```

Expected: `feature/glassmorphism-redesign` ブランチがGitHubにプッシュされる。
