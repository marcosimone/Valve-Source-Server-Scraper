# Valve-Source-Server-Scraper
This is a python program used to scrape server information from source servers
## Why though?
This was an exercise to practice networking and interpreting bytestreams from packets.  I also had to add the ability for split packets and out of order packets.  I used [this page](https://developer.valvesoftware.com/wiki/Source_Server_Queries "Source Server Queries") to help with the data interpretation.

This project was born out of curiosity and boredom while looking at the tf2 server browser.
## Usage
```

usage:
        connect.py <IP> <PORT> [ipr]

ipr can be in any order:
        i - print server info
        p - print player info
        r - print rules

```

## Example Usage
```
marcosimone> python source_server_scrape.py 74.201.57.61 27015 ipr

SERVER INFO
--------------------
steamid: 6634
map: pl_yamashiro_medieval_b3
protocol: 17
name:  rxg | 10x Mayhem RANDOMIZER | Reflex-Gamers.com
max_players: 30
vac: 1
servertype: d
visibility: 0
port: 27015
environment: l
players: 15
game: Team Fortress
version: 3963112
keywords: 010,10x,alltalk,gamers,increased_maxplayers,mayhem,misc,multiply,norespawntime,payload,randomizer,reflex,rxg,stats,ten,tf20,time
bots: 0
folder: tf
gameid_64: 440
id: 440
edf: 177
--------------------

PLAYER INFO
--------------------
name: daryl_g_ang
score: 11
duration: 3010.402100
--------------------
name: Snufflux
score: 13
duration: 2603.764893
--------------------
name: bumcaker
score: 0
duration: 1914.253174
--------------------
name: Meikyuu Minato
score: 71
duration: 1471.033203
--------------------
name: Übermensch
score: 25
duration: 1350.133179
--------------------
name: Zack Infamous
score: 12
duration: 1329.028198
--------------------
name: The MinecraftMaster
score: 23
duration: 1052.728271
--------------------
name: elkatras
score: 19
duration: 932.249573
--------------------
name: Game151
score: 11
duration: 834.164612
--------------------
name: [AG] Eeveedude the Fox Prophet
score: 3
duration: 516.539246
--------------------
name: Birdperson
score: 4
duration: 515.774475
--------------------
name: [B.A.P]
score: 6
duration: 490.019653
--------------------
name: Krystek Myca
score: 2
duration: 362.039642
--------------------
name: ГАНТОР-ПИНГВИН
score: 0
duration: 216.389664
--------------------
name: Finn the Human
score: 0
duration: 198.149643
--------------------

RULES
--------------------
207
tf_passtime_powerball_decayamount : 1
tf_arena_force_class : 0
eof_version : 2.6
tf_mm_servermode : 0
sv_cheats : 0
sv_pausable : 0
tf_passtime_experiment_instapass : 0
mp_weaponstay : 0
tf_mm_strict : 0
tf_gamemode_sd : 0
tf_passtime_throwarc_engineer : 0.2f
tf_powerup_mode : 0
tf_classlimit : 0
tf_passtime_save_stats : 0
mp_maxrounds : 0
tf_passtime_throwarc_sniper : 0.0f
sv_specnoclip : 1
tf_passtime_experiment_telepass : 0
mp_tournament : 0
sv_rollangle : 0
sv_tags : 10,10x,alltalk,gamers,increased_maxplayers,mayhem,misc,multiply,norespawntime,payload,randomizer,reflex,rxg,stats,ten,tf20,time
decalfrequency : 60
r_AirboatViewDampenDamp : 1.0
tf_weapon_criticals_melee : 1
tf_passtime_experiment_autopass : 0
tf_passtime_ball_sphere_collision : 1
tf_gamemode_pd : 0
mp_fadetoblack : 0
mp_tournament_readymode_min : 2
sv_waterfriction : 1
tv_enable : 0
sv_noclipspeed : 5
tf2items_manager : 1
tf_passtime_ball_inertia_scale : 1.0f
tf2items_manager_version : 1.4.3
tf_spec_xray : 1
sv_maxusrcmdprocessticks : 24
tf_passtime_mode_homing_speed : 1000.0f
mp_scrambleteams_auto_windifference : 2
r_JeepViewDampenFreq : 7.0
brimmunity_version : 1.1.0.rxg1
tf_passtime_powerball_threshold : 80
mp_match_end_at_timelimit : 0
sv_registration_successful : 0
sv_voiceenable : 1
tf_mm_trusted : 0
serves_bacon : YES
sv_password : 0
sm_updater_version : 1.2.2
sv_specspeed : 3
sv_alltalk : 1
tf2items_rnd_normals : 0
sv_vote_quorum_ratio : 0.6
sv_friction : 4
tf_passtime_powerball_decaysec_neutral : 1.5f
sourcemod_version : 1.8.0.5946
tf_passtime_ball_reset_time : 15
tf_playergib : 1
mp_footsteps : 1
tf_passtime_throwspeed_soldier : 800.0f
tf_max_charge_speed : 750
mp_friendlyfire : 0
tf_weapon_criticals : 1
tf_passtime_throwspeed_engineer : 850.0f
sv_footsteps : 1
tf_arena_use_queue : 1
mp_windifference : 0
mp_forcerespawn : 0
r_JeepViewDampenDamp : 1.0
tf_passtime_player_reticles_friends : 2
tf_passtime_throwarc_heavy : 0.175f
sm_betherobot_version : 1.3
tf_passtime_ball_model : models/passtime/ball/passtime_ball.mdl
r_AirboatViewZHeight : 0.0
tf_passtime_powerball_decay_delay : 10
tf_passtime_flinch_boost : 0
tf_passtime_throwarc_medic : 0.0f
nextlevel :
tf_birthday : 0
tf_gamemode_arena : 0
tf_passtime_scores_per_round : 5
sv_contact : ROKER
sv_maxspeed : 320
tf_passtime_pack_range : 512
tf_mvm_death_penalty : 0
sm_spray_version : 5.8a
tf2items_rnd_version : 1.591
tf_gamemode_passtime : 0
tf_passtime_ball_seek_range : 128
tf_passtime_ball_takedamage_force : 800.0f
sv_stepsize : 18
tf_passtime_overtime_idle_sec : 5
tf_passtime_throwspeed_velocity_scale : 0.33f
mp_winlimit : 0
tf_spells_enabled : 0
tf_gamemode_mvm : 0
tf_gamemode_tc : 0
tf_gamemode_ctf : 0
tf_passtime_ball_mass : 1.0f
sv_specaccelerate : 5
tf_medieval_autorp : 1
tf_passtime_powerball_maxairtimebonus : 100
tf_passtime_ball_damping_scale : 0.01f
mp_timelimit : 35
mp_disable_respawn_times : 1
mp_windifference_min : 0
tf_passtime_throwspeed_spy : 900.0f
tf_damage_disablespread : 1
tf_gamemode_rd : 0
mp_tournament_readymode : 0
tv_relaypassword : 0
sv_gravity : 800
mp_stalemate_meleeonly : 0
tf_passtime_throwarc_demoman : 0.15f
tf_halloween_allow_truce_during_boss_event : 1
mp_flashlight : 1
mp_teamlist : hgrunt;scientist
tf_gamemode_misc : 1
mp_autoteambalance : 1
tf_medieval : 0
mp_autocrosshair : 1
tf_passtime_pack_hp_per_sec : 2.0f
tf_bot_count : 0
tf_use_fixed_weaponspreads : 0
sv_rollspeed : 200
sourceirc_version : 0.2 (build 3)
mp_tournament_readymode_team_size : 0
mp_respawnwavetime : 10.0
tf_allow_player_use : 0
tf_passtime_throwarc_pyro : 0.1f
tf_passtime_throwspeed_demoman : 850.0f
tf_passtime_mode_homing_lock_sec : 1.5f
sv_accelerate : 10
tf_passtime_throwarc_spy : 0.0f
tf_passtime_powerball_decaysec : 4.5f
tf_force_holidays_off : 0
deathmatch : 1
tf_passtime_ball_takedamage : 1
r_AirboatViewDampenFreq : 7.0
mp_forceautoteam : 0
tf_passtime_throwspeed_sniper : 900.0f
tf2items_rnd_enabled : 1
tf_gamemode_payload : 1
mp_holiday_nogifts : 0
tf_passtime_powerball_airtimebonus : 40
mp_tournament_readymode_countdown : 10
tf_passtime_score_crit_sec : 5.0f
servertools_plugin_version : 3.0.5
mp_tournament_stopwatch : 1
tf_passtime_pack_speed : 1
tf_passtime_experiment_instapass_charge : 0
sv_registration_message : No account specified
sm_nextmap : pl_swiftwater_ugc
tf_passtime_speedboost_on_get_ball_time : 2.0f
thirdperson_version : 2.1.0
r_VehicleViewDampen : 1
tf_arena_round_time : 0
tf_passtime_steal_on_melee : 1
tf_arena_max_streak : 3
tf_gamemode_cp : 0
sm_advertisements_version : 1.0.4
tf_passtime_throwspeed_medic : 900.0f
tf2attributes_version : 1.2.1
sv_noclipaccelerate : 5
tf_arena_change_limit : 1
sv_stopspeed : 100
sv_steamgroup :
tf_mvm_min_players_to_start : 3
tf_passtime_throwspeed_pyro : 750.0f
tf_arena_preround_time : 10
tf_overtime_nag : 0
tf_ctf_bonus_time : 10
sv_airaccelerate : 10
tf_gravetalk : 1
tf_passtime_throwspeed_heavy : 850.0f
coop : 0
tf_passtime_throwspeed_scout : 700.0f
sb_version : 1.4.11
tv_password : 0
improved_map_randomizer_version : 3.4.5
r_JeepViewZHeight : 10.0
mp_stalemate_enable : 0
tf_server_identity_disable_quickplay : 0
tf_passtime_ball_sphere_radius : 7.2f
mp_fraglimit : 0
tf_player_name_change_time : 60
tf_passtime_throwarc_soldier : 0.1f
sv_wateraccelerate : 10
tf_arena_override_cap_enable_time : -1
mp_highlander : 0
tf_passtime_ball_drag_coefficient : 0.01f
tf_arena_first_blood : 1
tf2items_version : 1.6.3
mp_scrambleteams_auto : 1
tf_spawn_glows_duration : 10
tf_passtime_ball_rotdamping_scale : 1.0f
tf_passtime_player_reticles_enemies : 1
tf_passtime_powerball_passpoints : 25
tf_passtime_ball_seek_speed_factor : 3f
metamod_version : 1.10.6-devV
mp_teamplay : 0
tf_beta_content : 0
mp_falldamage : 1
tf_passtime_throwarc_scout : 0.1f
tf_passtime_teammate_steal_time : 45
sv_bounce : 0
mp_allowNPCs : 1
--------------------
```
