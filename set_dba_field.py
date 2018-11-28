#import string
import sys
from xml.etree import cElementTree as etree
import requests
from time import sleep

DIRECTORY_URL = "https://xxxxxxxx/api/rest/v2/organizations/"

CREDS = ("ian.coxey@xxxxxxxx.com", "xxxxxxxx")

HEADERS = {"content-type": "application/xml"}


def change_dba_in_alc(ALC):
    getALC = requests.get(DIRECTORY_URL + ALC, auth=CREDS).content
    xml = etree.fromstring(getALC)
    elems = xml.findall('DoingBusinessAs')
    for elem in elems:
        elem.text = 'xxxxxxxx Insurance Agency'
    xmlnew = etree.tostring(xml)
    #print(xmlnew)
    response = requests.put(IXDIRECTORY_URL + ALC, headers={"Content-Type": "application/xml"},
                            auth=CREDS, data=xmlnew)

    if response.status_code != 200:
        print("Got {} trying to update quote:\n\n{}".format(
            response.status_code, response.content
        ))
    print("updating", ALC)
    sleep(2)

ALCs = [
#"W40321F",
#"W40525F",
#"W9000082F",
#"W510000F",
"W684498EF",
"W49718F",
"W747192KF",
"W7471932F",
"W49721F",
"W684497TF",
"W49690F",
"W40085F",
"W40286F",
"W7471970F",
"W49676F",
"W40392F",
"W40094F",
"W40044F",
"W40180F",
"W40071F",
"W747293FF",
"W40252F",
"W40127F",
"W6844440F",
"W40357F",
"W7471960F",
"W40238F",
"W49680F",
"W40493F",
"W68441FPF",
"W40503F",
"W40223F",
"W40220F",
"W7471953F",
"W40577F",
"W40034F",
"W9000014F",
"W40398F",
"W771932RF",
"W40253F",
"W7471979F",
"W9000067F",
"W40480F",
"W7471974F",
"W40584F",
"W9000071F",
"W41960F",
"W684494KF",
"W40228F",
"W40040F",
"W68441GFF",
"W40440F",
"W40424F",
"W747191AF",
"W40530F",
"W68441EVF",
"W40290F",
"W968215PF",
"W49695F",
"W49684F",
"W49723F",
"W40436F",
"W6844998F",
"W684591RF",
"W40068F",
"W40294F",
"W40219F",
"W40178F",
"W9000021F",
"W40204F",
"W40353F",
"W40489F",
"W40070F",
"W684494CF",
"W40098F",
"W40478F",
"W40344F",
"W40447F",
"W747292EF",
"W40582F",
"W40038F",
"W40154F",
"W40244F",
"W40444F",
"W68441CTF",
"W40243F",
"W40211F",
"W40152F",
"W6844449F",
"W684413FF",
"W40236F",
"W40073F",
"W684495AF",
"W968215NF",
"W49706F",
"W684598KF",
"W49697F",
"W684419AF",
"W40145F",
"W6845993F",
"W684592CF",
"W49699F",
"W9000061F",
"W40376F",
"W9000008F",
"W40074F",
"W40157F",
"W40254F",
"W40349F",
"W40052F",
"W40060F",
"W40097F",
"W40100F",
"W684594FF",
"W40233F",
"W40283F",
"W40390F",
"W40396F",
"W68441EHF",
"W9000048F",
"W40041F",
"W7471996F",
"W40011F",
"W40338F",
"W40541F",
"W9000020F",
"W40456F",
"W40555F",
"W40310F",
"W68441ATF",
"W6844939F",
"W40189F",
"W968215MF",
"W40163F",
"W40441F",
"W40549F",
"W40122F",
"W40153F",
"W40255F",
"W40102F",
"W40457F",
"W40057F",
"W9000064F",
"W40217F",
"W40213F",
"W7472968F",
"W9000043F",
"W40300F",
"W40528F",
"W40080F",
"W49711F",
"W684493XF",
"W500687F",
"W7472953F",
"W460AAF",
"W40412F",
"W40332F",
"W40177F",
"W9000073F",
"W40125F",
"W40193F",
"W40201F",
"W9000010F",
"W40571F",
"W40229F",
"W40378F",
"W40352F",
"W40137F",
"W40142F",
"W40181F",
"W40050F",
"W40150F",
"W645938TF",
"W40182F",
"W7472995F",
"W40237F",
"W9000065F",
"W40316F",
"W40345F",
"W40590F",
"W40389F",
"W49683F",
"W684595AF",
"W40471F",
"W40477F",
"W40166F",
"W9000052F",
"W68441FEF",
"W68441FGF",
"W40546F",
"W747191TF",
"W49678F",
"W40148F",
"W40333F",
"W40416F",
"W40042F",
"W40516F",
"W684518RF",
"W40278F",
"W40517F",
"W9000068F",
"W40388F",
"W668212MF",
"W684593LF",
"W40199F",
"W40231F",
"W40246F",
"W40566F",
"W40551F",
"W9000066F",
"W40319F",
"W747191EF",
"W9000055F",
"W40578F",
"W40309F",
"W40308F",
"W40479F",
"W49729F",
"W68451FKF",
"W49724F",
"W49696F",
"W68451FRF",
"W40258F",
"W747296AF",
"W968215XF",
"W40314F",
"W40526F",
"W7471915F",
"W7472106F",
"W6317605F",
"W6844478F",
"W40296F",
"W684594RF",
"W40599F",
"W40536F",
"W40078F",
"W40176F",
"W684419CF",
"W40420F",
"W40539F",
"W40481F",
"W6844923F",
"W40160F",
"W500651F",
"W9000044F",
"W49700F",
"W747295NF",
"W49713F",
"W40206F",
"W40216F",
"W7472903F",
"W747191XF",
"W500694F",
"W968216F",
"W9000085F",
"W6825936F",
"W968037RF",
"W40315F",
"W40343F",
"W7472966F",
"W40144F",
"W747293EF",
"W40417F",
"W40143F",
"W40560F",
"W684518PF",
"W684598XF",
"W500603F",
"W684496PF",
"W747192LF",
"W684495NF",
"W40585F",
"W40575F",
"W40362F",
"W40291F",
"W40331F",
"W40263F",
"W40450F",
"W40120F",
"W684595PF",
"W7471972F",
"W50061PF",
"W500664F",
"W68441F1F",
"W40469F",
"W40459F",
"W40586F",
"W40249F",
"W40564F",
"W40115F",
"W9000076F",
"W40318F",
"W40164F",
"W40028F",
"W40476F",
"W40439F",
"W49692F",
"W40380F",
"W40379F",
"W40445F",
"W40130F",
"W40274F",
"W40597F",
"W40341F",
"W40542F",
"W68451FNF",
"W9000018F",
"W40131F",
"W40162F",
"W9000036F",
"W40350F",
"W40518F",
"W6815341F",
"W684593EF",
"W49707F",
"W49710F",
"W40108F",
"W40000F",
"W40270F",
"W40351F",
"W40537F",
"W40139F",
"W40317F",
"W40184F",
"W684492WF",
"W49693F",
"W684497GF",
"W6844990F",
"W50061LF",
"W90012N",
"W49730F",
"W40207F",
"W49709F",
"W684514RF",
"W6844420F",
"W49685F",
"W9000087F",
"W6845942F",
"W49715F",
"W49717F",
"W509M4WF",
"W49716F",
"W50022HF",
"W9000079F",
"W40556F",
"W40185F",
"W40501F",
"W9000001F",
"W40292F",
"W7471958F",
"W40260F",
"W40281F",
"W40482F",
"W40037F",
"W40250F",
"W6844436F",
"W40061F",
"W40205F",
"W40355F",
"W9000069F",
"W40124F",
"W40499F",
"W40053F",
"W40195F",
"W40256F",
"W6844973F",
"W68441FTF",
"W40502F",
"W50032AF",
"W684594VF",
"W40167F",
"W40463F",
"W40119F",
"W9000077F",
"W40059F",
"W40230F",
"W68451CNF",
"W40132F",
"W40490F",
"W40521F",
"W68441CWF",
"W40437F",
"W7471802F",
"W40133F",
"W40158F",
"W49677F",
"W40225F",
"W40266F",
"W40303F",
"W40451F",
"W40312F",
"W40381F",
"W40529F",
"W747191CF",
"W7471964F",
"W7471978F",
"W40210F",
"W40583F",
"W40324F",
"W7471907F",
"W40339F",
"W40096F",
"W40191F",
"W40221F",
"W40298F",
"W49698F",
"W40407F",
"W68441EXF",
"W40433F",
"W7472975F",
"W6844805F",
"W747192TF",
"W7471980F",
"W684495EF",
"W40545F",
"W40081F",
"W40400F",
"W40592F",
"W68441F4F",
"W40399F",
"W49686F",
"W747293JF",
"W40043F",
"W40146F",
"W40104F",
"W6471927F",
"W40086F",
"W40186F",
"W40209F",
"W6844942F",
"W500259F",
"W684596LF",
"W40103F",
"W40330F",
"W40568F",
"W68451F4F",
"W40505F",
"W40496F",
"W40543F",
"W40046F",
"W9000005F",
"W68459B6F",
"W40311F",
"W40088F",
"W40118F",
"W40288F",
"W6599057F",
"W747193JF",
"W9000034F",
"W40561F",
"W40382F",
"W49679F",
"W40329F",
"W41964F",
"W40340F",
"W747291KF",
"W49688F",
"W40474F",
"W49714F",
"W684597TF",
"W40565F",
"W40488F",
"W747192FF",
"W49687F",
"W40161F",
"W40383F",
"W684494GF",
"W40394F",
"W40174F",
"W40200F",
"W9000045F",
"W40497F",
"W40550F",
"W40257F",
"W40165F",
"W40092F",
"W9000080F",
"W684511Lf",
"W40337F",
"W40169F",
"W40035F",
"W40141F",
"W40039F",
"W500671F",
"W40084F",
"W40594N",
"W40594F",
"W40101F",
"W6845913F",
"W40113F",
"W771913RF",
"W40196F",
"W40265F",
"W7471950F",
"W49726F",
"W7471995F",
"W49725F",
"W49722F",
"W49712F",
"W747291NF",
"W684597LF",
"W684491KF",
"W984491RF",
"W49691F",
"W6459M58F",
"W40572F",
"W40175F",
"W40364F",
"W40426F",
"W40402F",
"W40087F",
"W40093F",
"W40326F",
"W6844804F",
"W40361F",
"W40531F",
"W40099F",
"W40126F",
"W40532F",
"W40136F",
"W9000023F",
"W40435F",
"W40491F",
"W40544F",
"W40462F",
"W40251F",
"W7190523F",
"W40470F",
"W500662F",
"W40411F",
"W40135F",
"W9000070F",
"W40224F",
"W500682F",
"W40356F",
"W7472913F",
"W500654F",
"W40573F",
"W40054F",
"W68441EGF",
"W40268F",
"W9000002F",
"W40090F",
"W9000078F",
"W40259F",
"W9000011F",
"W68451EAF",
"W40218F",
"W40222F",
"W40248F",
"W40276F",
"W9000026F",
"W6844959F",
"W9000028F",
"W40325F",
"W550061F",
"W40419F",
"W40494F",
"W40313F",
"W40076F",
"W40275F",
"W9000019F",
"W40504F",
"W6844984F",
"W40261F",
"W40538F",
"W40036F",
"W684592NF",
"W40301F",
"W6100000F",
"W7100000F",
"W40128F",
"W9000030F",
"W9000035F",
"W40234F",
"W7471997F",
"W40595F",
"W684493HF",
"W9000027F",
"W68441CEF",
"W40570F",
"W40442F",
"W40289F",
"W40410F",
"W68441G4F",
"W9000049F",
"W40159F",
"W40443F",
"W684593JF",
"W40202F",
"W684516FF",
"W40069F",
"W49702F",
"W500621F",
"W49727F",
"W49701F",
"W40187F",
"W40534F",
"W40242F",
"W500618F",
"W49681F",
"W40467F",
"W500632F",
"W40226F",
"W40413F",
"W40448F",
"W68215LF",
"W40600F",
"W41332F",
"W40484F",
"W40055F",
"W747293MF",
"W40519F",
"W7471993F",
"W7471923F",
"W40574F",
"W40051F",
"W40535F",
"W40403F",
"W40021F",
"W40557F",
"W40475F",
"W40523F",
"W40297F",
"W49694F",
"W9000088F",
"W49703F",
"W40587F",
"W684597CF",
"W40045F",
"W40192F",
"W40284F",
"W40418F",
"W40596F",
"W40438F",
"W40272F",
"W68441CGF",
"W40307F",
"W40129F",
"W40409F",
"W40452F",
"W40305F",
"W40591F",
"W40269F",
"W40492F",
"W40512F",
"W40123F",
"W40466F",
"W9000037F",
"W40172F",
"W40079F",
"W747192EF",
"W9000047F",
"W40342F",
"W49689F",
"W40235F",
"W40212F",
"W40170F",
"W40422F",
"W7471904F",
"W40203F",
"W40072F",
"W40117F",
"W40173F",
"W40465F",
"W684493VF",
"W68451EGF",
"W40540F",
"W40138F",
"W684416RF",
"W49708F",
"W49682F",
"W49704F",
"W49705F",
"w747292gf",
"W747192NF",
"W747144EF",
"W49728F",
"W6060125F",
"W684496RF",
"W6610226F",
"W40049F",
"W40346F",
"W40306F",
"W40179F",
"W9000016F",
"W40366F",
"W40580F",
"W6844965F",
"W40106F",
"W684592KF",
"W40455F",
"W684494PF",
"W40062F",
"W40267F",
"W40334F",
"W40063F",
"W40277F",
"W40581F",
"W40111F",
"W40065F",
"W40458F",
"W684494EF",
"W40464F",
"W68451A7F",
"W68451A7Z",
"W40562F",
"W40589F",
"W40520F",
"W40593F",
"W40067F",
"W40147F",
"W40404F",
"W6844439F",
"W7472937F",
"W40116F",
"W9000042F",
"W40507F",
"W7472955F",
"W40232F",
"W40245F",
"W40487F",
"W6844807F",
"W40522F",
"W40285F",
"W40105F",
"W9000017F",
"W40214F",
"W40247F",
"W40197F",
"W41967F",
"W9000083F",
"W49719F",
"W9000074F",
"W6844945F",
"W40588F",
"W40384F",
"W6844131F",
"W40434F",
"W40553F",
"W40527F",
"W40320F",
"W40064F",
"W40327F",
"W40322F",
"W40414F",
"W6845916F",
"W9000022F",
"W684596G7",
"W684596GF",
"W40082F",
"W68441FNF",
"W9000081F",
"W968212MF",
"W7471994F",
"W968037PF",
"W6844927F",
"W7472942F",
"W50061CF",
"W40509F",
"W40302F",
"W40348F",
"W6845802F",
"W500688F",
"W6815313F",
"W40485F",
"W49675F",
"W40510F",
"W9000015F",
"W40323F",
"W40558F",
"W500644F",
"W500648F",
"W40511F",
"W9000038F",
"W40287F",
"W684494TF",
"W9000033F",
"W9000009F",
"W40282F",
"W40386F",
"W40385F",
"W40121F",
"W9000075F",
"W7471982F",
"W6060997F",
"W9000084F",
"W9000004F",
"W40156F",
"W40579F",
"W40415F",
"W40408F",
"W40454F",
"W40387F",
"W40095F",
"W40446F",
"W40513F",
"W6844430F",
"W49720F",
"W9000086F",
"W40075F",
"W40500F",
"W40406F",
"W9000003F",
"W40240F",
"W747192HF",
"W7471969F",
"W40168F",
"W40109F",
"W9000040F",
"W40056F",
"W684493NF",
"W9000006F",
"W40114F",
"W7471989F",
"W40598F",
"W9000024F",
"W9000072F",
"W40548F",
"W40569F",
"W9000053F",
"W9000054F",
"W40112F",
"W40401F",
"W6845989F",
"W7471986F",
"W7471913F",
"W7471911F",
"W40360F"

]



if __name__ == "__main__":
    for ALC in ALCs:
        change_dba_in_alc(ALC)