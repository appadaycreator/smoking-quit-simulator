LEGACY_HTML = True  # 既存HTMLを保持（再アセンブル禁止）
TITLE = '禁煙計算【無料】タバコをやめると何年で何万円節約できる？'
DESCRIPTION = '禁煙計算を完全無料でお使いいただけます。登録不要・スマートフォン対応のWebツールです。'
JS_CODE = 'var timeline=[\n  {time:"20分後",emoji:"❤️",desc:"心拍数・血圧が正常値に近づき始める"},\n  {time:"12時間後",emoji:"🫁",desc:"血液中の一酸化炭素濃度が正常レベルに回復"},\n  {time:"2週間〜3ヶ月後",emoji:"🏃",desc:"血液循環が改善し、肺機能が30%向上"},\n  {time:"1〜9ヶ月後",emoji:"🌬️",desc:"咳・息切れが減少。肺の自己回復が進む"},\n  {time:"1年後",emoji:"💪",desc:"心臓病リスクが喫煙者の半分に低下"},\n  {time:"5年後",emoji:"🧠",desc:"脳卒中リスクが非喫煙者と同レベルに"},\n  {time:"10年後",emoji:"🫀",desc:"肺がんリスクが喫煙者の半分に低下"},\n  {time:"15年後",emoji:"🏆",desc:"心臓病リスクが非喫煙者とほぼ同レベルに"}\n];\n\nfunction calculate(){\n  var cigs=parseInt(document.getElementById(\'cigs-per-day\').value)||10;\n  var priceBox=parseInt(document.getElementById(\'price-per-box\').value)||580;\n  var years=parseInt(document.getElementById(\'years-smoking\').value)||15;\n  var invest=document.getElementById(\'invest-type\').value;\n\n  var cigsPerBox=20;\n  var dailyCost=cigs/cigsPerBox*priceBox;\n  var monthly=Math.round(dailyCost*30);\n  var annual=Math.round(dailyCost*365);\n\n  var rates={save:0.001,nisa:0.04,stock:0.06};\n  var r=rates[invest]/12;\n  var months10=120;var months30=360;\n\n  function futureValue(monthlyPayment,months,monthlyRate){\n    if(monthlyRate===0)return monthlyPayment*months;\n    return monthlyPayment*((Math.pow(1+monthlyRate,months)-1)/monthlyRate);\n  }\n  var fv10=futureValue(monthly,months10,r);\n  var fv30=futureValue(monthly,months30,r);\n\n  document.getElementById(\'r-monthly\').textContent=\'¥\'+monthly.toLocaleString();\n  document.getElementById(\'r-annual\').textContent=\'¥\'+annual.toLocaleString();\n  document.getElementById(\'r-10yr\').textContent=\'¥\'+Math.round(fv10/10000)+\'万\';\n  document.getElementById(\'r-investment\').textContent=\'¥\'+Math.round(fv30/10000)+\'万\';\n\n  var tlEl=document.getElementById(\'timeline\');tlEl.innerHTML=\'\';\n  timeline.forEach(function(t){\n    var d=document.createElement(\'div\');d.className=\'timeline-item\';\n    d.innerHTML=\'<span class="text-xl flex-shrink-0">\'+t.emoji+\'</span><div><strong class="text-green-700">\'+t.time+\'</strong><div class="text-gray-600">\'+t.desc+\'</div></div>\';\n    tlEl.appendChild(d);\n  });\n\n  var clinicCost=15000;\n  var clinicPayback=Math.ceil(clinicCost/monthly);\n  document.getElementById(\'r-clinic-compare\').textContent=\'禁煙外来費用（保険適用）は約\'+clinicCost.toLocaleString()+\'円。禁煙成功すれば\'+clinicPayback+\'ヶ月で元が取れます。自力禁煙の成功率は3〜5%に対し、禁煙外来では30〜40%と大幅に向上します。\';\n\n  document.getElementById(\'results\').style.display=\'block\';\n  document.getElementById(\'affiliate-section\').style.display=\'block\';\n  document.getElementById(\'results\').scrollIntoView({behavior:\'smooth\'});\n}'
MAIN_HTML = '<div><button class="btn">開始する</button></div>'
FAQ = [
    ('禁煙計算は無料で使えますか？', 'はい、完全無料・登録不要でご利用いただけます。'),
    ('何回でも使えますか？', 'はい、回数制限なく何度でもご利用いただけます。'),
    ('入力したデータはサーバーに送信されますか？', 'いいえ。すべての処理はブラウザ内で完結し、入力内容はサーバーへ送信されません。'),
    ('スマートフォンでも使えますか？', 'はい、スマートフォン・タブレット・PCすべてに最適化されています。'),
    ('結果を保存・共有できますか？', 'スクリーンショットでの保存またはSNSシェアボタンからご共有いただけます。'),
]
HOW_TO = [
    'ページを開き、入力フォームの項目を確認する',
    '必要な情報を入力または選択する',
    '実行ボタンをクリックして結果を取得する',
    '表示された結果・アドバイスを確認する',
    '必要に応じてコピー・SNSシェアで活用する',
]
FOOTER_LINKS = [('https://appadaycreator.com/sleep-quality-checker/', '睡眠の質チェッカー'), ('https://appadaycreator.com/bmi-body-tracker/', 'BMI・体重管理'), ('https://appadaycreator.com/household-budget-analyzer/', '家計簿診断')]
