__author__ = 'root'

from EventCoder import EventCoder
#from mongo_client import insert

def map_articles(articleText):
    return articleText.encode('utf-8')


def code_articles(articleText, petrGlobals={}):
    coder = EventCoder(petrGlobal = petrGlobals)
    events_map = coder.gen_cameo_event(map_articles(articleText))
    return str(events_map)


def code_articles_(articleText, petrGlobals={}):
    coder = EventCoder(petrGlobal = petrGlobals)
    events_map = coder.gen_cameo_event(articleText)
    return str(events_map)



if __name__ == "__main__":


    coder = EventCoder(petrGlobal={})

    #article = '{ "type" : "story", "doc_id" : "nytasiapacific20160622.0002", "head_line" : "Lightning Ridge Journal: An Amateur Undertaking in Australian Mining Town With No Funeral Home", "date_line" : "Tue, 21 Jun 2016 03:52:15 GMT", "sentences" : [ { "sentence_id" : 1, "sentence" : "A Tunisian court has jailed a Nigerian student for two years for helping young militants join an armed Islamic group in Lebanon, his lawyer said Wednesday.", "parse_sentence" : "(ROOT (S (S (NP (DT A) (NNP Tunisian) (NN court)) (VP (VBZ has) (VP (VBN jailed) (NP (DT a) (NNP Nigerian) (NN student)) (PP (IN for) (NP (NP (CD two) (NNS years)) (PP (IN for) (S (VP (VBG helping) (S (NP (JJ young) (NNS militants)) (VP (VB join) (NP (DT an) (JJ armed) (JJ Islamic) (NN group)) (PP (IN in) (NP (NNP Lebanon))))))))))))) (, ,) (NP (PRP$ his) (NN lawyer)) (VP (VBD said) (NP (NNP Wednesday))) (. .)))" } ], "corref" : "" }'

    article = """{
	"type":"story",
	"doc_id":"hindu_cities20160829.0009",
	"head_line":"Velankanni festival begins",
	"date_line" : "Tue, 21 Jun 2016 03:52:15 GMT",
	"sentences":[
		{
			"sentence_id":1,
			"sentence":"NAGAPATTINAM :TAMILNADU: 29/08/2016 : Our Lady of Health Velankanni Basilica Annual Flag hoisting, in progress, as thousands of devotees witnessing, in Nagapattinam district.Photo: B.Velankanni Raj  The 11-day annual feast of Shrine Basilica of Our Lady of Health, popularly called Annai Velankanni Matha, began in Velankanni on Monday evening with a huge procession and hoisting of the holy flag by Most Rev. M. Devadass Ambrose, Bishop of Thanjavur.",
			"parse_sentence":"(ROOT (NP (NP (NNP NAGAPATTINAM)) (: :) (NP (NP (NNP TAMILNADU)) (: :) (NP (NP (CD 29/08/2016)) (: :) (NP (NP (NP (PRP$ Our) (NN Lady)) (PP (IN of) (NP (NP (NNP Health) (NNP Velankanni) (NN Basilica) (JJ Annual) (NN Flag)) (VP (VBG hoisting) (, ,) (PP (IN in) (NP (NN progress))) (, ,) (SBAR (IN as) (S (NP (NP (NP (NP (NNS thousands)) (PP (IN of) (NP (NNS devotees)))) (VP (VBG witnessing) (, ,) (PP (IN in) (NP (NNP Nagapattinam) (NNP district.Photo))))) (: :) (NP (NP (NNP B.Velankanni) (NNP Raj) (NNP The) (JJ 11-day) (JJ annual) (NN feast)) (PP (IN of) (NP (NP (NNP Shrine) (NN Basilica)) (PP (IN of) (NP (NP (PRP$ Our) (NN Lady)) (PP (IN of) (NP (NNP Health))))))) (, ,) (VP (ADVP (RB popularly)) (VBN called) (S (NP (NNP Annai) (NNP Velankanni) (NNP Matha)))) (, ,))) (VP (VBD began) (PP (IN in) (NP (NNP Velankanni))) (PP (IN on) (NP (NP (NNP Monday) (NN evening)) (PP (IN with) (NP (NP (DT a) (JJ huge) (NN procession)) (CC and) (NP (NP (NN hoisting)) (PP (IN of) (NP (DT the) (JJ holy) (NN flag))) (PP (IN by) (NP (JJS Most) (NNP Rev.) (NNP M.) (NNP Devadass) (NNP Ambrose))))))))))))))) (, ,) (NP (NP (NNP Bishop)) (PP (IN of) (NP (NNP Thanjavur))))))) (. .)))",
			"token":"NAGAPATTINAM,:,TAMILNADU,:,29/08/2016,:,Our,Lady,of,Health,Velankanni,Basilica,Annual,Flag,hoisting,,,in,progress,,,as,thousands,of,devotees,witnessing,,,in,Nagapattinam,district.Photo,:,B.Velankanni,Raj,The,11-day,annual,feast,of,Shrine,Basilica,of,Our,Lady,of,Health,,,popularly,called,Annai,Velankanni,Matha,,,began,in,Velankanni,on,Monday,evening,with,a,huge,procession,and,hoisting,of,the,holy,flag,by,Most,Rev.,M.,Devadass,Ambrose,,,Bishop,of,Thanjavur,.",
			"lemma":"NAGAPATTINAM,:,TAMILNADU,:,29/08/2016,:,we,lady,of,Health,Velankanni,basilica,annual,flag,hoist,,,in,progress,,,as,thousand,of,devotee,witness,,,in,Nagapattinam,district.Photo,:,B.Velankanni,Raj,The,11-day,annual,feast,of,Shrine,basilica,of,we,lady,of,Health,,,popularly,call,Annai,Velankanni,Matha,,,begin,in,Velankanni,on,Monday,evening,with,a,huge,procession,and,hoisting,of,the,holy,flag,by,most,Rev.,M.,Devadass,Ambrose,,,Bishop,of,Thanjavur,.",
			"ner":"(SET,Annual|annual),(ORGANIZATION,Shrine|Basilica|of|Our|Lady|of|Health),(DATE,Monday),(NUMBER,29/08/2016),(LOCATION,NAGAPATTINAM|Nagapattinam|Velankanni|Thanjavur),(DURATION,11-day),(TIME,evening),(PERSON,Annai|Velankanni|Matha|M.|Devadass|Ambrose)",
			"relation":"",
			"sentiment":-1
		},
		{
			"sentence_id":2,
			"sentence":"Pilgrims from various parts of the country witnessed the flag hoisting ceremony.",
			"parse_sentence":"(ROOT (S (NP (NP (NNPS Pilgrims)) (PP (IN from) (NP (NP (JJ various) (NNS parts)) (PP (IN of) (NP (DT the) (NN country)))))) (VP (VBD witnessed) (S (NP (DT the) (NN flag)) (VP (VBG hoisting) (NP (NN ceremony))))) (. .)))",
			"token":"Pilgrims,from,various,parts,of,the,country,witnessed,the,flag,hoisting,ceremony,.",
			"lemma":"Pilgrims,from,various,part,of,the,country,witness,the,flag,hoist,ceremony,.",
			"ner":"",
			"relation":"",
			"sentiment":-1
		},
		{
			"sentence_id":3,
			"sentence":"Rev.Fr.A.M.Prabakar, Rector, and other priests of the shrine were present.",
			"parse_sentence":"(ROOT (S (NP (NP (NNP Rev.Fr.A.M.Prabakar)) (, ,) (NP (NNP Rector)) (, ,) (CC and) (NP (NP (JJ other) (NNS priests)) (PP (IN of) (NP (DT the) (NN shrine))))) (VP (VBD were) (ADJP (JJ present))) (. .)))",
			"token":"Rev.Fr.A.M.Prabakar,,,Rector,,,and,other,priests,of,the,shrine,were,present,.",
			"lemma":"Rev.Fr.A.M.Prabakar,,,Rector,,,and,other,priest,of,the,shrine,be,present,.",
			"ner":"(DATE,present)",
			"relation":"",
			"sentiment":-1
		},
		{
			"sentence_id":4,
			"sentence":"The illuminated and colourful car procession carrying the idol of Our Lady of Health would be held on September 7 and the lowering of Our Lady's flag on September 8.",
			"parse_sentence":"(ROOT (S (S (NP (NP (DT The) (ADJP (VBN illuminated) (CC and) (JJ colourful)) (NN car) (NN procession)) (VP (VBG carrying) (NP (NP (DT the) (NN idol)) (PP (IN of) (NP (NP (PRP$ Our) (NN Lady)) (PP (IN of) (NP (NNP Health)))))))) (VP (MD would) (VP (VB be) (VP (VBN held) (PP (IN on) (NP (NNP September) (CD 7))))))) (CC and) (S (NP (NP (DT the) (NN lowering)) (PP (IN of) (NP (NP (PRP$ Our) (NN Lady) (POS \u0027s)) (NN flag)))) (PP (IN on) (NP (NNP September) (CD 8)))) (. .)))",
			"token":"The,illuminated,and,colourful,car,procession,carrying,the,idol,of,Our,Lady,of,Health,would,be,held,on,September,7,and,the,lowering,of,Our,Lady,\u0027s,flag,on,September,8,.",
			"lemma":"the,illuminate,and,colourful,car,procession,carry,the,idol,of,we,lady,of,Health,would,be,hold,on,September,7,and,the,lowering,of,we,lady,\u0027s,flag,on,September,8,.",
			"ner":"(DATE,September|7|September|8)",
			"relation":"",
			"sentiment":-1
		},
		{
			"sentence_id":5,
			"sentence":"Holy mass would be held in various languages during the festival.",
			"parse_sentence":"(ROOT (S (NP (JJ Holy) (NN mass)) (VP (MD would) (VP (VB be) (VP (VBN held) (PP (IN in) (NP (JJ various) (NNS languages))) (PP (IN during) (NP (DT the) (NN festival)))))) (. .)))",
			"token":"Holy,mass,would,be,held,in,various,languages,during,the,festival,.",
			"lemma":"holy,mass,would,be,hold,in,various,language,during,the,festival,.",
			"ner":"",
			"relation":"",
			"sentiment":-1
		},
		{
			"sentence_id":6,
			"sentence":"The district administration and the Basilica authorities have made elaborate arrangements and provided basic amenities including protected drinking water and sanitary facilities to a large number of pilgrims attending the festival.",
			"parse_sentence":"(ROOT (S (NP (NP (DT The) (NN district) (NN administration)) (CC and) (NP (DT the) (NN Basilica) (NNS authorities))) (VP (VBP have) (VP (VP (VBN made) (NP (JJ elaborate) (NNS arrangements))) (CC and) (VP (VBN provided) (NP (NP (JJ basic) (NNS amenities)) (PP (VBG including) (NP (NP (JJ protected) (NN drinking) (NN water)) (CC and) (NP (NP (JJ sanitary) (NNS facilities)) (PP (TO to) (NP (NP (DT a) (JJ large) (NN number)) (PP (IN of) (NP (NP (NNS pilgrims)) (VP (VBG attending) (NP (DT the) (NN festival)))))))))))))) (. .)))",
			"token":"The,district,administration,and,the,Basilica,authorities,have,made,elaborate,arrangements,and,provided,basic,amenities,including,protected,drinking,water,and,sanitary,facilities,to,a,large,number,of,pilgrims,attending,the,festival,.",
			"lemma":"the,district,administration,and,the,basilica,authority,have,make,elaborate,arrangement,and,provide,basic,amenity,include,protected,drinking,water,and,sanitary,facility,to,a,large,number,of,pilgrim,attend,the,festival,.",
			"ner":"",
			"relation":"",
			"sentiment":-1
		},
		{
			"sentence_id":7,
			"sentence":"The police have made security arrangements for the pilgrims who came by special trains and buses.",
			"parse_sentence":"(ROOT (S (NP (DT The) (NNS police)) (VP (VBP have) (VP (VBN made) (NP (NP (NN security) (NNS arrangements)) (PP (IN for) (NP (NP (DT the) (NNS pilgrims)) (SBAR (WHNP (WP who)) (S (VP (VBD came) (PP (IN by) (NP (JJ special) (NNS trains) (CC and) (NNS buses))))))))))) (. .)))",
			"token":"The,police,have,made,security,arrangements,for,the,pilgrims,who,came,by,special,trains,and,buses,.",
			"lemma":"the,police,have,make,security,arrangement,for,the,pilgrim,who,come,by,special,train,and,bus,.",
			"ner":"",
			"relation":"",
			"sentiment":-1
		}
	],
	"corref":""
}"""
    print(code_articles(article, coder.get_PETRGlobals()))




