Kamputerm
=========

Слоўнік беларускай кампутарнай тэрміналёґіі


Кароткая нататка пра фармат зыходніка слоўніка
----------------------------------------------

Зыходнікам слоўніка ёсьць XML-файл. Далей коратка разгледзім ягоны фармат.
Больш падрабязнае апісаньне чытайце
[тут](http://code.google.com/p/stardict-3/source/browse/dict/doc/TextualDictionaryFileFormat).
Кожны артыкул мае наступную структуру:

~~~{.xml}
<article>
	<key>termin</key>
	<synonym>synonim</synonym>
	<definition type="h" kind="al"><![CDATA[
		пераклад]]>
	</definition>
</article>
~~~

Кожны артыкул канечне мусіць мець адзін ці болей тэґаў `<key>`. Кожны тэґ
зьмяшчае адзін з варыянтаў напісаньня мэтавага тэрміна. Прыклады: *disc* i
*disk*, *@* і *commercial at* і т. д.

Кожны артыкул можа мець тэґ (ці тэґі) `<sysnony>`. У ім зьмяшчаецца іншы
тэрмін, каторы мае падобнае блізкае значэньне.

Тэґ `<definition>` утрымлівае пераклад тэрміна. Ён заўсёды мусіць мець
два атрыбуты: `type` і `kind`. Атрыбут `type` заўсёды мае значэньне "h".  Гэта значыць, што зьвесткамі ўнутры тэґа ёсьць html-код. Атрыбут `kind`
можа мець наступныя значэньні:

- `be` — пераклад у клясычным правапісе;
- `by` — пераклад у школьным правапісе;
- `al` — калі розныя правапісы аднолькавыя, каб не дубляваць;
- `mt` — пералік сустрэчаў на каторых абмяркоўваўся тэрмін;
- `rm` — розныя заўвагі.

Цяпер падрабязьней разгледзеім кожны тып тэґа `<definition>`.

### Атрыбуты *be*, *by* і *al*

Калі пераклад — гэта адназначны поўны беларускі адпаведнік, то запісвайце
ўласна яго без аніякага фарматаваньне. Калі гэта дзеяслоў, то канечне 
запісвайце формы незакончанага й закончанага трэваньня (менавіта ў такім
парадку).

Калі тэрмін мае некалькі сэнсаў то розныя сэнсы запісвайце з дапамогах
htlm-сьпісаў `lo` з рымскімі лічбамі. Для гэтага дадайце атрыбут `type="I"`:

~~~{.html}
<lo type="I">
<li>першы пераклад</li>
<li>другі пераклад</li>
</lo>
~~~

Для тэрмінаў, каторыя могуць быць рознымі часьцінамі мовы, трэба таксама
выкарыстоўваць сьпісы, але ўжо з арабскімі літарамі (гэта стандартна для
тэґа `lo`). Перад перакладам трэба пазначыць што гэта за часьціна мовы:
*verb*, *noutn*, *adj.*, *adv.* і інш. Гэты пазнакі разам з усімі іншымі
граматычнымі пазнакамі трэба замыкаць у тэґ `<em>`.

Рознага кшталту тлумачэньні варта запісаваць у тэґу `<i>`.

### Атрыбут *mt* (meetting)

У вызначэньнях з атрыбутам `mt` ідзе пералік сустрэчаў праз коску на каторых
абмяркоўваўся тэрмін.

### Атрыбут *rm* (remark)

Гэта камэнтар у якім пазначаюцца розныя заўвагі, у тым ліку пазнака таго, 
што тэрмін яшчэ не канчаткова вызначаны.

Некалькі тыповых прыкладаў артыкулаў
------------------------------------

~~~{.xml}
<article>
	<key>localized</key>
	<definition type="h" kind="be">лякалізава́ны</definition>
	<definition type="h" kind="by">лакалізава́ны</definition>
	<definition type="h" kind="mt">18</definition>
</article>
~~~

~~~{.xml}
<article>
	<key>log in</key>
	<synonym>log on</synonym>
	<synonym>sign in</synonym>
	<definition type="h" kind="be">уваходзіць, увайсьці́</definition>
	<definition type="h" kind="by">уваходзіць, увайсці́</definition>
	<definition type="h" kind="mt">22</definition>
</article>
~~~

~~~{.xml}
<article>
	<key>close</key>
	<definition type="h" kind="al"><![CDATA[
		<ol type="I">
		<li>зачыня́ць, зачыні́ць <i>(файл, акно)</i></li>
		<li> <i>(зрабіць недаступным для іншых)</i>
			<ol>
		    <li><em>verb</em> закрыва́ць, закры́ць</li>
		    <li><em>adj.</em> закры́ты</li>
			</ol>
		</li>
		</ol>]]>
	</definition>
	<definition type="h" kind="mt">2, 3</definition>
	<definition type="h" kind="rm">на перагляд</definition>
</article>
~~~

Карыстаньне скрыптамі
---------------------

У тэчцы `bin/` знаходзяцца скрыпты для канвэртаваньня ў наступныя фарматы:

- html
- tab — выкарыстоўваецца ў OmegaT
- qph — qt phrase books. Выкарыстоўваецца ў Qt Linguist

Каб атрымаць больш дакладную даведку, выканайце скрыпт з арґумэнтам `--help`.

Прыклады выкарыстаньня скрыптоў:

~~~{.bash}
quendi@quendi-desktop:~/Develop/Workspace/kamputerm$ cd bin/
quendi@quendi-desktop:~/Develop/Workspace/kamputerm/bin$ ls -l
усяго 16
-rwxrwxr-x 1 quendi quendi 1432 Снж 30 23:02 tab2qph.py
-rwxr-xr-x 1 quendi quendi 4465 Снж 30 14:40 xml2html.py
-rwxrwxr-x 1 quendi quendi 2947 Стд  1 17:28 xml2tab.py
quendi@quendi-desktop:~/Develop/Workspace/kamputerm/bin$ ./xml2html.py ../src/kamputerm.xml -o kamputerm.html
quendi@quendi-desktop:~/Develop/Workspace/kamputerm/bin$ ls
kamputerm.html  tab2qph.py  xml2html.py  xml2tab.py
quendi@quendi-desktop:~/Develop/Workspace/kamputerm/bin$ ./xml2tab.py --orthography=classic -o kamputerm.txt ../src/kamputerm.xml 
quendi@quendi-desktop:~/Develop/Workspace/kamputerm/bin$ ls
kamputerm.html  kamputerm.txt  tab2qph.py  xml2html.py  xml2tab.py
quendi@quendi-desktop:~/Develop/Workspace/kamputerm/bin$ head kamputerm.txt 
@	сьліма́к
add-in	дада́так
add-on	дада́так
adjust	наста́віць, адрэґулява́ць
alarm	noun аля́рмverb алярмава́ць, залярмава́ць
alert	апаве́шчаньне, перасьцярога
align	раўнава́ць, зраўнава́ць
align left	раўнава́ць зьлева, зраўнава́ць зьлева
align right	раўнава́ць справа, зраўнава́ць справа
animate	анімава́ць, занімава́ць
quendi@quendi-desktop:~/Develop/Workspace/kamputerm/bin$ cat kamputerm.txt | ./tab2qph.py > kamputerm.qph
quendi@quendi-desktop:~/Develop/Workspace/kamputerm/bin$ ls
kamputerm.html  kamputerm.qph  kamputerm.txt  tab2qph.py  xml2html.py  xml2tab.py
quendi@quendi-desktop:~/Develop/Workspace/kamputerm/bin$ 
~~~

