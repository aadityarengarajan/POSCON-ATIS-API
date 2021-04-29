from flask import redirect, render_template, Flask, request, url_for, send_file
import requests

app = Flask(__name__)


@app.route('/<icao>')
def runway_determiner(icao):

    ATIS = requests.get(f"https://services.poscon.com/atis/{icao}").json()["atis"]
    content = ATIS["body"]

    content = content.split(".")

    returnable = {"icao":icao,
                  "runways":[]}

    def check_notification(notification):

        if "APPROACH" in notification:
            notification.replace("APPROACH IN USE","")
            runways = notification.split(",")
            for runway in runways:
                if len(runway.split("RWYS"))>1:
                    if runway.split("RWYS")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RWYS")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : runway.split("RWYS")[0]}})
                elif len(runway.split("RY"))>1:
                    if runway.split("RY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : runway.split("RY")[0]}})
                elif len(runway.split("RWY"))>1:
                    if runway.split("RWY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: eturnable["runways"].append({"runway":runway.split("RWY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : runway.split("RWY")[0]}})
                else:
                    returnable["runways"].append({"runway":runway,
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "unknown"}})

        elif "APCH" in notification:
            print(notification)
            notification.replace("APCH","")
            runways = notification.split(",")
            for runway in runways:
                if len(runway.split("RWYS"))>1:
                    if runway.split("RWYS")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RWYS")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : runway.split("RWYS")[0]}})
                elif len(runway.split("RY"))>1:
                    if runway.split("RY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : runway.split("RY")[0]}})
                elif len(runway.split("RWY"))>1:
                    if runway.split("RWY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RWY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : runway.split("RWY")[0]}})
                else:
                    if runway.strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway,
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "unknown"}})

        elif "ARR" in notification:
            notification.replace("ARR","")
            runways = notification.split(",")
            for runway in runways:
                if len(runway.split("RWYS"))>1:
                    if runway.split("RWYS")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RWYS")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : runway.split("RWYS")[0]}})
                elif len(runway.split("RY"))>1:
                    if runway.split("RY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : runway.split("RY")[0]}})
                elif len(runway.split("RWY"))>1:
                    if runway.split("RWY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RWY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : runway.split("RWY")[0]}})
                else:
                    if runway.strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway,
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "unknown"}})


        elif "ILS" in notification:
            notification = notification.replace("ILS","")
            runways = notification.split(",")
            for runway in runways:
                if len(runway.split("RWY"))>1:
                    if runway.split("RWY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RWY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "ILS"}})
                elif len(runway.split("RY"))>1:
                    if runway.split("RY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "ILS"}})
                elif len(runway.split("RWY"))>1:
                    if runway.split("RWY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RWY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "ILS"}})
                else:
                    if runway.strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway,
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "ILS"}})

        elif "VISUAL" in notification.upper():
            notification = notification.upper().replace("VISUAL","")
            runways = notification.upper().split(",")
            for runway in runways:
                if len(runway.split("RWY"))>1:
                    if runway.split("RWY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RWY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "VISUAL"}})
                elif len(runway.split("RY"))>1:
                    if runway.split("RY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "VISUAL"}})
                elif len(runway.split("RWY"))>1:
                    if runway.split("RWY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RWY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "VISUAL"}})
                else:
                    if runway.strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway,
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "VISUAL"}})

        elif "VOR" in notification:
            notification = notification.replace("VOR","")
            runways = notification.split(",")
            for runway in runways:
                if len(runway.split("RWY"))>1:
                    if runway.split("RWY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RWY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "VOR"}})
                elif len(runway.split("RY"))>1:
                    if runway.split("RY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "VOR"}})
                elif len(runway.split("RWY"))>1:
                    if runway.split("RWY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RWY")[-1].strip(),
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "VOR"}})
                else:
                    if runway.strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway,
                                                  "type" : {"operation" : "approach",
                                                            "approach" : "VOR"}})


        if "DEPG" in notification:
            notification = notification.replace("DEPG","")
            runways = notification.split(",")
            for runway in runways:
                if len(runway.split("RWYS"))>1:
                    if runway.split("RWYS")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True:     returnable["runways"].append({"runway":runway.split("RWYS")[-1].strip(),
                                                      "type" : {"operation" : "departure"}})
                elif len(runway.split("RY"))>1:
                    if runway.split("RY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RY")[-1].strip(),
                                                  "type" : {"operation" : "departure"}})
                elif len(runway.split("RWY"))>1:
                    if runway.split("RWY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RWY")[-1].strip(),
                                                  "type" : {"operation" : "departure"}})
                else:
                    if runway.strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.strip(),
                                                  "type" : {"operation" : "departure"}})

        elif "DEP" in notification:
            notification = notification.replace("DEP","")
            runways = notification.split(",")
            for runway in runways:
                if len(runway.split("RWYS"))>1:
                    if runway.split("RWYS")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True:     returnable["runways"].append({"runway":runway.split("RWYS")[-1].strip(),
                                                      "type" : {"operation" : "departure"}})
                elif len(runway.split("RY"))>1:
                    if runway.split("RY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RY")[-1].strip(),
                                                  "type" : {"operation" : "departure"}})
                elif len(runway.split("RWY"))>1:
                    if runway.split("RWY")[-1].strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.split("RWY")[-1].strip(),
                                                  "type" : {"operation" : "departure"}})
                else:
                    if runway.strip().replace("R","").replace("L","").replace("C","").isnumeric()==True: returnable["runways"].append({"runway":runway.strip(),
                                                  "type" : {"operation" : "departure"}})

    for notification in content:
        check_notification(notification)
        

    if content == ['']:
        content_dep = ATIS["departure"].split(".")
        content_arr = ATIS["arrival"].split(".")

        for notification in content_dep:
            check_notification(notification)
        for notification in content_arr:
            check_notification(notification)

    final_returnables = []

    og_returnable = returnable

    for i in returnable["runways"]:
        RWY_ADDED = False
        if i["type"]["operation"] == "approach":
            if i["type"]["approach"] == "unknown":
                for x in returnable["runways"]:
                    if i["runway"].strip() == x["runway"].strip():
                        if x["type"]["operation"] == "approach":
                            if x["type"]["approach"]!="unknown":
                                final_returnables.append(x)
                                RWY_ADDED = True
        if RWY_ADDED == False:
            final_returnables.append(i)
            RWY_ADDED = True

    returnables = []

    for i in final_returnables:
        if i not in returnables : returnables.append(i)

    returnable["runways"] = returnables

    return str(str(returnable)+"<br/><br/>"+str(ATIS))


if __name__=="__main__":
    app.run(
        debug=True,
        use_reloader=True,
        use_debugger=True,
        port=8080,
        host='0.0.0.0',
        use_evalex=True,
        threaded=True,
        passthrough_errors=False
        )