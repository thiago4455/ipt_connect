# coding: utf8
from django.urls import re_path

from .parameters import instance_name
from .forms import member_for_team
from .tactics import *

app_name = instance_name

urlpatterns = [
    re_path(r"^$", tournament_overview),
    re_path(r"^tournament$", tournament_overview, name="tournament_overview"),
    re_path(r"^participants$", participants_overview, name="participants_overview"),
    re_path(
        r"^participants/(?P<pk>[0-9]+)/$", participant_detail, name="participant_detail"
    ),
    re_path(r"^jurys$", jurys_overview, name="jurys_overview"),
    re_path(r"^member_for_team$", member_for_team),
    re_path(r"^jurys/(?P<pk>[0-9]+)/$", jury_detail, name="jury_detail"),
    re_path(r"^problems$", problems_overview, name="problems_overview"),
    re_path(r"^problems/(?P<pk>[0-9]+)/$", problem_detail, name="problem_detail"),
    re_path(r"^rounds$", rounds, name="rounds"),
    re_path(r"^rounds/(?P<pk>[0-9]+)/$", round_detail, name="round_detail"),
    re_path(r"^round_add_next/(?P<pk>[0-9]+)/$", round_add_next, name="round_add_next"),
    re_path(r"^teams$", teams_overview, name="teams"),
    re_path(
        r"^teams/(?P<team_name>[A-Za-z0-9\w|\W\- ]+)/$", team_detail, name="team_detail"
    ),
    re_path(r"^physics_fights$", rounds, name="rounds"),
    re_path(r"^physics_fights/$", rounds, name="rounds"),
    re_path(
        r"^physics_fights/(?P<pfid>[0-9]+)/$",
        physics_fight_detail,
        name="physics_fight_detail",
    ),
    re_path(r"^ranking$", ranking, name="ranking"),
    re_path(r"^build_tactics$", build_tactics),
    re_path(r"^poolranking$", poolranking, name="poolranking"),
    re_path(r"^export_csv_ranking_timeline$", export_csv_ranking_timeline),
    re_path(r"^participants_export$", participants_export),
    re_path(r"^participants_export_web$", participants_export_web),
    re_path(r"^participants_all$", participants_all),
    re_path(r"^jury_export$", jury_export),
    re_path(r"^jury_export_csv$", jury_export_csv),
    re_path(r"^jury_export_web$", jury_export_web),
    re_path(r"^trombinoscope$", participants_trombinoscope),
    re_path(r"^soon", soon),
    re_path(r"^update_all", update_all, name="update_all"),
    re_path(r"^verify_all", verify_all, name="verify_all"),
    re_path(r"^upload_csv", upload_csv, name="upload_csv"),
    re_path(r"^upload_problems", upload_problems, name="upload_problems"),
]
