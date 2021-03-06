enum MessageDirection : uint8_t {
    ERROR = '!',
    MULTIWII_TO_COM = '>',
    COM_TO_MULTIWII = '<'
};

enum MessageProtocol : uint8_t {
    MULTIWII_PROTOCOL = 'M',
    PHOENIX_RC_PROTOCOL = 'R',
    PHOENIX_LED_PROTOCOL = 'L',
    PHOENIX_SCANNER_PROTOCOL = 'S'
};

enum MessageCode : uint8_t {
    SCANNER_READING = 45,
    SCANNER_RESTART = 46,
    MARVIC_LED_0 = 50,
    MARVIC_LED_1 = 51,
    MARVIC_LED_2 = 52,
    MARVIC_LED_3 = 53,
    MARVIC_LED_4 = 54,
    MARVIC_LED_5 = 55,
    MARVIC_SINGLE_LED = 56,
    MARVIC_BATTERY = 66,
    MARVIC_SONAR = 68,
    MARVIC_INFRA_RED = 69,
    MARVIC_LIDAR = 70,
    MARVIC_BAROMETER = 71,
    MARVIC_SERVO_SMALL = 90,
    MARVIC_SERVO_BIG = 91,
    MARVIC_IDENTIFIER = 100,
    MULTIWII_STATUS = 101,
    MULTIWII_IMU = 102,
    MULTIWII_SERVO = 103,
    MULTIWII_MOTOR = 104,
    MULTIWII_RC = 105,
    MULTIWII_RC_PILOT = 113,
    MULTIWII_GPS = 106,
    MULTIWII_PID = 112,
    MULTIWII_GPS_WP = 118,
    MULTIWII_ATTITUDE = 108,
    MULTIWII_ALTITUDE = 109,
    MULTIWII_MOTOR_SET = 214,           // setting motor
    MULTIWII_RC_SET = 200,              // setting rc
    MULTIWII_SET_RAW_GPS = 201,
    MULTIWII_PID_SET = 202,
    MULTIWII_GPS_WP_SET = 209           // setting gps way point
};

enum MessageLength : uint8_t {
    REQUEST = 0,
    SCANNER_READING_LENGTH = 6,
    SCANNER_RESTART_LENGTH = 2,
    MARVIC_BATTERY_LENGTH = 8,
    MARVIC_SONAR_LENGTH = 6,
    MARVIC_LIDAR_LENGTH = 6,
    MARVIC_INFRA_RED_LENGTH = 6,
    MARVIC_BAROMETER_LENGTH = 6,
    MARVIC_STRIP_LED_LENGTH = 30,
    MARVIC_SINGLE_LED_LENGTH = 5,
    MARVIC_SERVO_SMALL_LENGTH = 8,
    MARVIC_SERVO_BIG_LENGTH = 36,
    MARVIC_IDENTIFIER_LENGTH = 4,
    MULTIWII_STATUS_LENGTH = 11,
    MULTIWII_IMU_LENGTH = 18,
    MULTIWII_SERVO_LENGTH = 16,
    MULTIWII_MOTOR_LENGTH = 16,
    MULTIWII_RC_LENGTH = 16,
    MULTIWII_RC_PILOT_LENGTH = 16,
    MULTIWII_GPS_LENGTH = 16,
    REQUEST_GPS_WP = 1,
    MULTIWII_GPS_WP_LENGTH = 18,
    MULTIWII_ATTITUDE_LENGTH = 6,
    MULTIWII_ALTITUDE_LENGTH = 6,
    MULTIWII_MOTOR_SET_LENGTH = 16,
    MULTIWII_RC_SET_LENGTH = 16,
    MULTIWII_PID_SET_LENGTH = 30,
    MULTIWII_GPS_WP_SET_LENGTH = 18
};

struct Payload {
    union {
        struct {
            uint16_t distance_scanner_1;
            uint16_t distance_scanner_2;
            uint16_t measurement_index;
        } scanner_distance;

        struct {
            uint16_t angles;
        } scanner_restart;

        struct {
            uint8_t p1;     uint8_t i1;     uint8_t d1;     // roll
            uint8_t p2;     uint8_t i2;     uint8_t d2;     // pitch
            uint8_t p3;     uint8_t i3;     uint8_t d3;     // yaw
            uint8_t p4;     uint8_t i4;     uint8_t d4;     // alt
            uint8_t p5;     uint8_t i5;     uint8_t d5;     // vel
            uint8_t p6;     uint8_t i6;     uint8_t d6;     // pos
            uint8_t p7;     uint8_t i7;     uint8_t d7;     // posrate
            uint8_t p8;     uint8_t i8;     uint8_t d8;     // navrate
            uint8_t p9;     uint8_t i9;     uint8_t d9;     // level
            uint8_t p10;    uint8_t i10;    uint8_t d10;    // mag
        } multiwii_pid;

        struct {
            uint8_t led_0_r;    uint8_t led_0_g;    uint8_t led_0_b;
            uint8_t led_1_r;    uint8_t led_1_g;    uint8_t led_1_b;
            uint8_t led_2_r;    uint8_t led_2_g;    uint8_t led_2_b;
            uint8_t led_3_r;    uint8_t led_3_g;    uint8_t led_3_b;
            uint8_t led_4_r;    uint8_t led_4_g;    uint8_t led_4_b;
            uint8_t led_5_r;    uint8_t led_5_g;    uint8_t led_5_b;
            uint8_t led_6_r;    uint8_t led_6_g;    uint8_t led_6_b;
            uint8_t led_7_r;    uint8_t led_7_g;    uint8_t led_7_b;
            uint8_t led_8_r;    uint8_t led_8_g;    uint8_t led_8_b;
            uint8_t led_9_r;    uint8_t led_9_g;    uint8_t led_9_b;
        } marvic_led_strip;                 // MARVIC_LED_0 = 50, MARVIC_LED_1 = 51, MARVIC_LED_2 = 52, MARVIC_LED_3 = 53

        struct {
            uint8_t strip_index;
            uint8_t led_id;
            uint8_t led_r;  uint8_t led_g;  uint8_t led_b;
        } marvic_led_single;                // MARVIC_SINGLE_LED = 54

        struct {
            uint8_t strip_index;            // 0: only strip 0    1: only strip 1    2: only strip 2    3: only strip 3    4: all strips
            uint8_t mode;                   // 0: full off    1: continuous    2: blink    3: half-blink    4: pulse    5: half-pulse    6: special position light (e.g. continuous base color and last led heart beating white)
            uint8_t alarm;                  // scales blink or pulse speed or special position external blink color (0: white-OK, 1: blue-GPSposhold, 2: red-BatteryLow)
            uint8_t led_r;                  // base color
            uint8_t led_g;                  // base color
            uint8_t led_b;                  // base color
        } marvic_led_mode;                  // MARVIC_MODE_LED = 55

        struct {
            uint32_t millisecond_time_stamp;
            uint16_t distance;
        } marvic_altitude;                  // MARVIC_SONAR = 68, MARVIC_INFRA_RED = 69, MARVIC_LIDAR = 70, MARVIC_BAROMETER = 71

        struct {
            uint16_t cell1_mean;
            uint16_t cell2_mean;
            uint16_t cell3_mean;
            uint16_t cell4_mean;
        } marvic_battery;

        struct {
            uint16_t cycleTime;
            uint16_t i2c_errors_count;
            uint16_t sensor;
            uint32_t flag;
            uint8_t global_conf;
        } multiwii_status;

        struct {
            uint8_t version;
            uint8_t type;
            uint8_t empty0;
            uint8_t empty1;
        } identifier;

        struct {
            int16_t accx;   int16_t accy;   int16_t accz;
            int16_t gyrx;   int16_t gyry;   int16_t gyrz;
            int16_t magx;   int16_t magy;   int16_t magz;
        } multiwii_raw_imu;

        struct {
            uint16_t servo0;    uint16_t servo1;    uint16_t servo2;    uint16_t servo3;
            uint16_t servo4;    uint16_t servo5;    uint16_t servo6;    uint16_t servo7;
            uint16_t servo8;    uint16_t servo9;    uint16_t servo10;   uint16_t servo11;
            uint16_t servo12;   uint16_t servo13;   uint16_t servo14;   uint16_t servo15;
            uint16_t servo16;   uint16_t servo17;
        } marvic_servo;

        struct {
            uint16_t servo0;    uint16_t servo1;    uint16_t servo2;    uint16_t servo3;
        } marvic_servo_small;

        struct {
            uint16_t motor0;    uint16_t motor1;
            uint16_t motor2;    uint16_t motor3;
            uint16_t motor4;    uint16_t motor5;
            uint16_t motor6;    uint16_t motor7;
        } multiwii_motor;

        struct {
            uint16_t motor0;    uint16_t motor1;
            uint16_t motor2;    uint16_t motor3;
            uint16_t motor4;    uint16_t motor5;
            uint16_t motor6;    uint16_t motor7;
        } multiwii_motor_set;

        struct {
            uint16_t roll;
            uint16_t pitch;
            uint16_t yaw;
            uint16_t throttle;
            uint16_t aux1;  uint16_t aux2;  uint16_t aux3;  uint16_t aux4;
            uint16_t aux5;  uint16_t aux6;  uint16_t aux7;  uint16_t aux8;
        } multiwii_rc;

        struct {
            uint16_t roll;
            uint16_t pitch;
            uint16_t yaw;
            uint16_t throttle;
            uint16_t aux1;  uint16_t aux2;  uint16_t aux3;  uint16_t aux4;
        } multiwii_rc_set;

        struct {
            uint8_t fix;
            uint8_t numSat;
            uint8_t coordLAT;   uint8_t coordLAT1;  uint8_t coordLAT2;  uint8_t coordLAT3;
            uint8_t coordLON;   uint8_t coordLON1;  uint8_t coordLON2;  uint8_t coordLON3;
            uint16_t altitude;
            uint16_t speed;
            uint16_t ground_course;
        } multiwii_gps;

        struct {
            uint8_t wp_number;
            uint8_t coordLAT;   uint8_t coordLAT1;  uint8_t coordLAT2;  uint8_t coordLAT3;
            uint8_t coordLON;   uint8_t coordLON1;  uint8_t coordLON2;  uint8_t coordLON3;
            uint8_t altitude;   uint8_t altitude1;  uint8_t altitude2;  uint8_t altitude3;
            uint16_t heading;
            uint16_t stay_time;
            uint8_t nav_flag;
        } multiwii_gps_way_point;

        struct {
            int16_t roll;
            int16_t pitch;
            int16_t yaw;
        } multiwii_attitude;

        struct {
            int32_t estAlt;
            uint16_t variation;
        } multiwii_altitude;

        struct {
            uint8_t wp_number;
            uint8_t coordLAT;   uint8_t coordLAT1;  uint8_t coordLAT2;  uint8_t coordLAT3;
            uint8_t coordLON;   uint8_t coordLON1;  uint8_t coordLON2;  uint8_t coordLON3;
            uint8_t altitude;   uint8_t altitude1;  uint8_t altitude2;  uint8_t altitude3;
            uint16_t heading;
            uint16_t stay_time;
            uint8_t nav_flag;
        } multiwii_gps_set_way_point;
    };
};

struct Message {
    uint8_t msg_preamble;
    MessageProtocol msg_protocol;
    MessageDirection msg_direction;
    MessageLength msg_length;
    MessageCode msg_code;
    Payload msg_data;
    uint8_t checksum;
};
