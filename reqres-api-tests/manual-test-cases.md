# API Test Cases - ReqRes.in
# GET /api/users Endpoint

## Test Implementation
**Framework**: SeleniumBase with Python
**File**: [test_record_video.py](test_record_video.py)
**Cloudflare Bypass**: Undetected Chrome Driver (`--uc` mode)
**Video Recording**: pyscreenrec (auto-enabled for all tests)

## Endpoint Information
- **URL**: `https://reqres.in/api/users`
- **Method**: GET
- **Query Parameter**: `page` (optional, default: 1)
- **Description**: Retrieve a paginated list of users

---

## Test Cases

### TC001: Valid Request with Page=2

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=2` | Status code is 200 |
| 2 | Verify response structure | Response contains `page`, `per_page`, `total`, `total_pages`, `data`, and `support` fields |
| 3 | Verify page value | `page` equals 2 |
| 4 | Verify data array | `data` array contains exactly 6 user objects |
| 5 | Verify user object structure | Each user has `id`, `email`, `first_name`, `last_name`, and `avatar` fields |
| 6 | Verify user IDs | IDs are unique integers (7, 8, 9, 10, 11, 12) |
| 7 | Verify email format | All emails follow valid email format |
| 8 | Verify avatar URLs | All avatar URLs are valid HTTPS URLs |

**Implementation**: [test_record_video.py:81](test_record_video.py#L81)
**Status**: ✅ PASSED

---

### TC002: Valid Request with Page=1

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=1` | Status code is 200 |
| 2 | Verify response structure | Response structure matches expected schema |
| 3 | Verify page value | `page` equals 1 |
| 4 | Verify data array | `data` array contains exactly 6 user objects |
| 5 | Verify user IDs | IDs are unique integers (1, 2, 3, 4, 5, 6) |

**Implementation**: [test_record_video.py:94](test_record_video.py#L94)
**Status**: ✅ PASSED

---

### TC003: Invalid Page Number (Zero)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=0` | Response defaults to page 1 |
| 2 | Verify response | `page` equals 1 (API defaults invalid pages to 1) |

**Implementation**: [test_record_video.py:106](test_record_video.py#L106)
**Status**: ✅ PASSED

---

### TC004: Invalid Page Number (Negative)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=-1` | Response returns -1 |
| 2 | Verify response | `page` equals -1 (API returns negative value as-is) |

**Implementation**: [test_record_video.py:117](test_record_video.py#L117)
**Status**: ✅ PASSED

---

### TC005: Invalid Page Number (Too Large)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=999` | Status code is 200 |
| 2 | Verify response | Data array is empty |

**Implementation**: [test_record_video.py:128](test_record_video.py#L128)
**Status**: ✅ PASSED

---

### TC006: No Page Parameter (Default to Page 1)

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users` | Status code is 200 |
| 2 | Verify page value | `page` defaults to 1 |
| 3 | Verify data array | `data` array has users |

**Implementation**: [test_record_video.py:139](test_record_video.py#L139)
**Status**: ✅ PASSED

---

### TC007: Invalid Data Type for Page

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=abc` | Response handles invalid input gracefully |
| 2 | Verify response | Returns error or defaults to page 1 |

**Implementation**: [test_record_video.py:151](test_record_video.py#L151)
**Status**: ✅ PASSED

---

### TC008: Pagination Metadata Verification

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=2` | Status code is 200 |
| 2 | Verify `per_page` | `per_page` equals 6 |
| 3 | Verify `total` | `total` equals 12 |
| 4 | Verify `total_pages` | `total_pages` equals 2 |
| 5 | Verify calculation | `total` = `per_page` × `total_pages` (6 × 2 = 12) |

**Implementation**: [test_record_video.py:162](test_record_video.py#L162)
**Status**: ✅ PASSED

---

### TC009: Support Object Verification

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=2` | Status code is 200 |
| 2 | Verify support object exists | Response contains `support` object |
| 3 | Verify support.url | `support.url` is a valid URL |
| 4 | Verify support.text | `support.text` is a non-empty string |

**Implementation**: [test_record_video.py:175](test_record_video.py#L175)
**Status**: ✅ PASSED

---

### TC010: Response Headers Verification

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=2` | Status code is 200 |
| 2 | Verify Content-Type header | `Content-Type` is `application/json` |
| 3 | Verify response time | Response time is under 2 seconds |

**Implementation**: [test_record_video.py:188](test_record_video.py#L188)
**Status**: ✅ PASSED

---

### TC011: Multiple Page Parameters

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=1&page=2` | API handles duplicate parameters gracefully |
| 2 | Verify response | Returns first or last page parameter value |

**Implementation**: [test_record_video.py:200](test_record_video.py#L200)
**Status**: ✅ PASSED

---

### TC012: Empty Page Parameter

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=` | API handles empty parameter gracefully |
| 2 | Verify response | Returns error or defaults to page 1 |

**Implementation**: [test_record_video.py:211](test_record_video.py#L211)
**Status**: ✅ PASSED

---

### TC013: Page Parameter with SQL Injection Attempt

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=1'OR'1'='1` | API sanitizes input |
| 2 | Verify response | Returns error or handles safely |

**Implementation**: [test_record_video.py:222](test_record_video.py#L222)
**Status**: ✅ PASSED

---

### TC014: Email Format Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=2` | Status code is 200 |
| 2 | Extract all emails | All emails match regex: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$` |
| 3 | Verify email domain | All emails end with `@reqres.in` |

**Implementation**: [test_record_video.py:233](test_record_video.py#L233)
**Status**: ✅ PASSED

---

### TC015: Avatar URL Validation

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=2` | Status code is 200 |
| 2 | Extract avatar URLs | All avatar URLs match pattern: `^https://reqres.in/img/faces/\\d+-image.jpg$` |
| 3 | Attempt to fetch one avatar image | Avatar image is accessible (status 200) |

**Implementation**: [test_record_video.py:246](test_record_video.py#L246)
**Status**: ✅ PASSED

---

### TC016: Page Number as Decimal

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=1.5` | API handles gracefully |
| 2 | Verify response | Returns page 1 or 2, or error message |

**Implementation**: [test_record_video.py:259](test_record_video.py#L259)
**Status**: ✅ PASSED

---

### TC017: Page Number with Special Characters

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=!@#$%` | API handles gracefully |
| 2 | Verify response | Returns error or default page |

**Implementation**: [test_record_video.py:270](test_record_video.py#L270)
**Status**: ✅ PASSED

---

### TC018: Extra Query Parameters

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send GET request to `https://reqres.in/api/users?page=2&extra=param` | API ignores extra parameters or returns error |
| 2 | Verify response | Still returns valid response for page 2 |

**Implementation**: [test_record_video.py:281](test_record_video.py#L281)
**Status**: ✅ PASSED

---

## Test Summary

| Test Case | Status | Notes |
|-----------|--------|-------|
| TC001 | ✅ PASSED | Valid request with page=2 |
| TC002 | ✅ PASSED | Valid request with page=1 |
| TC003 | ✅ PASSED | Page 0 defaults to page 1 |
| TC004 | ✅ PASSED | Negative page returns -1 |
| TC005 | ✅ PASSED | Page 999 returns empty data |
| TC006 | ✅ PASSED | No page parameter defaults to 1 |
| TC007 | ✅ PASSED | Invalid data type defaults to 1 |
| TC008 | ✅ PASSED | Pagination metadata correct |
| TC009 | ✅ PASSED | Support object exists |
| TC010 | ✅ PASSED | Response headers valid |
| TC011 | ✅ PASSED | Multiple page parameters handled |
| TC012 | ✅ PASSED | Empty page parameter defaults to 1 |
| TC013 | ✅ PASSED | SQL injection attempt handled safely |
| TC014 | ✅ PASSED | All emails have valid format |
| TC015 | ✅ PASSED | All avatar URLs are valid |
| TC016 | ✅ PASSED | Decimal page rounds to 1 |
| TC017 | ✅ PASSED | Special characters default to 1 |
| TC018 | ✅ PASSED | Extra parameters ignored |

**Total**: 18 passed out of 18 tests (100% pass rate)
